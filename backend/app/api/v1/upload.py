from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from app.services.upload_service import save_uploaded_file

router = APIRouter()


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):
    return save_uploaded_file(file)