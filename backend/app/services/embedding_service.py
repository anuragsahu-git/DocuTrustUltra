from sentence_transformers import SentenceTransformer
from app.database import collection

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def store_embeddings(document_id, chunks):
    texts = [chunk.page_content for chunk in chunks]

    embeddings = embedding_model.encode(texts)

    ids = [
        f"{document_id}_{i}"
        for i in range(len(chunks))
    ]

    metadatas = [
        chunk.metadata
        for chunk in chunks
    ]

    collection.add(
        ids=ids,
        embeddings=embeddings.tolist(),
        documents=texts,
        metadatas=metadatas
    )

    return len(chunks)