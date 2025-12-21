import argparse
import sys

from app.services.ingestion import ingest_docs


def main():
    parser = argparse.ArgumentParser(description="Ingest docs into Qdrant with embeddings.")
    parser.add_argument("--docs-dir", default="docs", help="Path to docs directory (default: docs)")
    parser.add_argument("--collection", default=None, help="Qdrant collection name (default from settings)")
    parser.add_argument("--embedding-model", default=None, help="Embedding model (default from settings)")
    parser.add_argument("--embedding-dim", type=int, default=None, help="Embedding dimension (default from settings)")
    parser.add_argument("--dry-run", action="store_true", help="Run without calling OpenAI/Qdrant")
    args = parser.parse_args()

    result = ingest_docs(
        docs_dir=args.docs_dir,
        collection=args.collection,
        embedding_model=args.embedding_model,
        embedding_dimensions=args.embedding_dim,
        dry_run=args.dry_run,
    )

    print(
        f"Ingestion complete: files={result.files_processed}, chunks={result.chunks_written}, "
        f"collection={result.collection}, dry_run={result.dry_run}"
    )


if __name__ == "__main__":
    sys.exit(main())

