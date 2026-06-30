from datetime import datetime
from uuid import uuid4


def create_document_metadata(
    filename: str,
    file_type: str,
    size: int,
):
    return {
        "_id": str(uuid4()),
        "filename": filename,
        "file_type": file_type,
        "size": size,
        "status": "uploaded",
        "chunks": 0,
        "embedding_status": False,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }