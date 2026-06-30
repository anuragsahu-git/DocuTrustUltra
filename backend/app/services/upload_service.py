import uuid
from pathlib import Path
from datetime import datetime

from app.services.parser_service import parse_document
from app.services.chunk_service import chunk_documents
from app.services.embedding_service import embedding_model
from app.database import collection


def process_document(file_path: str):

    # -----------------------------
    # Parse document
    # -----------------------------
    documents = parse_document(file_path)

    # -----------------------------
    # Chunk document
    # -----------------------------
    chunks = chunk_documents(documents)

    if len(chunks) == 0:
        raise Exception("No text found in document.")

    # -----------------------------
    # Document Metadata
    # -----------------------------
    document_id = str(uuid.uuid4())
    filename = Path(file_path).name
    upload_time = datetime.utcnow().isoformat()

    # -----------------------------
    # Prepare Data
    # -----------------------------
    texts = []
    metadatas = []
    ids = []

    for index, chunk in enumerate(chunks):

        texts.append(chunk.page_content)

        metadata = chunk.metadata.copy()

        metadata["source"] = filename
        metadata["document_id"] = document_id
        metadata["chunk_id"] = index + 1
        metadata["upload_time"] = upload_time

        metadatas.append(metadata)

        ids.append(str(uuid.uuid4()))

    # -----------------------------
    # Generate Embeddings
    # -----------------------------
    embeddings = embedding_model.encode(texts).tolist()

    # -----------------------------
    # Store in ChromaDB
    # -----------------------------
    collection.add(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas
    )

    # -----------------------------
    # Response
    # -----------------------------
    return {
        "status": "success",
        "document_id": document_id,
        "filename": filename,
        "chunks": len(texts),
        "uploaded_at": upload_time
    }