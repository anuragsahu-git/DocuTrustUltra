from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader,
    UnstructuredPowerPointLoader,
)


def parse_document(file_path: str):

    suffix = Path(file_path).suffix.lower()

    if suffix == ".pdf":
        loader = PyPDFLoader(file_path)

    elif suffix == ".docx":
        loader = Docx2txtLoader(file_path)

    elif suffix == ".pptx":
        loader = UnstructuredPowerPointLoader(file_path)

    elif suffix == ".txt":
        loader = TextLoader(file_path, encoding="utf-8")

    else:
        raise Exception(f"Unsupported file type: {suffix}")

    return loader.load()