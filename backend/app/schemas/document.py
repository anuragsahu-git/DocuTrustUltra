from pydantic import BaseModel
from datetime import datetime


class DocumentResponse(BaseModel):
    document_id: str
    filename: str
    file_type: str
    size: int
    status: str
    created_at: datetime