from datetime import datetime

from pydantic import BaseModel


class CanonicalDocument(BaseModel):
    document_id: str
    source_type: str
    source_id: str

    title: str
    mime_type: str
    source_url: str | None
    content_reference: str

    version: str
    checksum: str
    modified_at: datetime

    deleted: bool = False
