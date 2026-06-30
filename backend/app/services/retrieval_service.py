from sentence_transformers import SentenceTransformer
from langchain_core.documents import Document

from app.database import collection

model = SentenceTransformer("all-MiniLM-L6-v2")


def retrieve_documents(query: str, top_k: int = 5):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    documents = []

    docs = results.get("documents", [[]])[0]
    metas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    for text, metadata, distance in zip(docs, metas, distances):

        metadata = metadata or {}

        metadata["score"] = round(max(0.0, 1 - distance), 3)

        documents.append(
            Document(
                page_content=text,
                metadata=metadata
            )
        )

    return documents