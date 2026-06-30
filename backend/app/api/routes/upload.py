from pathlib import Path
import shutil

from fastapi import APIRouter, UploadFile, File

from app.services.upload_service import process_document

router = APIRouter()

UPLOAD_DIR = "data/uploads"

Path(UPLOAD_DIR).mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = process_document(file_path)

    return {
        "filename": file.filename,
        **result
    }