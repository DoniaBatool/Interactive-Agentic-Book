from typing import Any, Dict, Optional

from pydantic import BaseModel


class DocumentChunk(BaseModel):
    id: str
    text: str
    metadata: Dict[str, Any]


class IngestionResult(BaseModel):
    files_processed: int
    chunks_written: int
    collection: str
    dry_run: bool = False

