import hashlib
import os
import re
import uuid
from pathlib import Path
from typing import List, Optional, Sequence, Tuple

import tiktoken
from openai import OpenAI

from app.core.config import get_settings
from app.models.schemas.chunk import DocumentChunk, IngestionResult
from app.services.qdrant_client import get_qdrant_client, upsert_chunks


settings = get_settings()


def _hash_id(text: str, metadata: dict) -> str:
    """
    Generate a stable UUID-based ID for Qdrant from text + metadata.
    Qdrant expects IDs as unsigned integers or UUIDs; we use UUID5 for determinism.
    """
    base = f"{text}|{metadata}"
    return str(uuid.uuid5(uuid.NAMESPACE_URL, base))


def _approximate_split(text: str, max_tokens: int = 350) -> List[str]:
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(text)
    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk_tokens = tokens[i : i + max_tokens]
        chunks.append(enc.decode(chunk_tokens))
    return chunks


def _read_markdown_files(root: Path) -> List[Tuple[Path, str]]:
    files = []
    for path in root.rglob("*.md"):
        files.append((path, path.read_text(encoding="utf-8")))
    for path in root.rglob("*.mdx"):
        files.append((path, path.read_text(encoding="utf-8")))
    return files


def _extract_chapter(path: Path) -> str:
    # Derive a simple chapter name from filename or parent
    stem = path.stem.replace("-", " ").replace("_", " ")
    return stem.title()


HEADING_RE = re.compile(r"^#{1,6}\s+(.*)$")


def _chunk_file(path: Path, content: str) -> List[DocumentChunk]:
    chunks: List[DocumentChunk] = []
    current_section: Optional[str] = None

    blocks = [b.strip() for b in content.split("\n\n") if b.strip()]
    for block in blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if not lines:
            continue

        heading_match = HEADING_RE.match(lines[0])
        if heading_match:
            current_section = heading_match.group(1).strip()
            # If the block only contains a heading, continue to next block
            if len(lines) == 1:
                continue
            text = "\n".join(lines[1:]).strip()
        else:
            text = "\n".join(lines).strip()

        if not text:
            continue

        for piece in _approximate_split(text):
            metadata = {
                "path": str(path),
                "chapter": _extract_chapter(path),
                "section": current_section,
                "source": "docs",
            }
            chunk_id = _hash_id(piece, metadata)
            chunks.append(DocumentChunk(id=chunk_id, text=piece, metadata=metadata))
    return chunks


def embed_chunks(client: OpenAI, model: str, chunks: List[DocumentChunk]) -> List[Tuple[str, Sequence[float], dict]]:
    vectors_payloads: List[Tuple[str, Sequence[float], dict]] = []
    for chunk in chunks:
        embedding = client.embeddings.create(model=model, input=chunk.text).data[0].embedding
        payload = {"text": chunk.text, **chunk.metadata}
        vectors_payloads.append((chunk.id, embedding, payload))
    return vectors_payloads


def ingest_docs(
    docs_dir: str = "docs",
    collection: Optional[str] = None,
    embedding_model: Optional[str] = None,
    embedding_dimensions: Optional[int] = None,
    dry_run: bool = False,
) -> IngestionResult:
    collection = collection or settings.qdrant_collection
    embedding_model = embedding_model or settings.embedding_model
    embedding_dimensions = embedding_dimensions or settings.embedding_dimensions

    docs_path = Path(docs_dir)
    files = _read_markdown_files(docs_path)
    all_chunks: List[DocumentChunk] = []
    for path, content in files:
        all_chunks.extend(_chunk_file(path, content))

    if dry_run or not settings.openai_api_key or not settings.qdrant_url:
        return IngestionResult(
            files_processed=len(files),
            chunks_written=len(all_chunks),
            collection=collection,
            dry_run=True,
        )

    openai_client = OpenAI(api_key=settings.openai_api_key)
    vectors_payloads = embed_chunks(openai_client, embedding_model, all_chunks)
    q_client = get_qdrant_client()
    written = upsert_chunks(q_client, collection, vectors_payloads, embedding_dimensions)

    return IngestionResult(
        files_processed=len(files),
        chunks_written=written,
        collection=collection,
        dry_run=False,
    )

