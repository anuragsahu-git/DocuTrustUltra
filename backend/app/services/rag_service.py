from app.services.retrieval_service import retrieve_documents
from app.services.generation_service import generate_answer

CONFIDENCE_THRESHOLD = 0.70


def ask_question(question: str):

    documents = retrieve_documents(question)

    if not documents:
        return {
            "answer": "I couldn't find that information in the uploaded documents.",
            "sources": []
        }

    best_score = documents[0].metadata.get("score", 0)

    if best_score < CONFIDENCE_THRESHOLD:
        return {
            "answer": "I couldn't find that information in the uploaded documents.",
            "sources": []
        }

    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    answer = generate_answer(question, context)

    sources = []

    for doc in documents:

        sources.append(
            {
                "document": doc.metadata.get("source", "Uploaded Document"),
                "page": doc.metadata.get("page", 1),
                "chunk": (
                    doc.page_content[:300] + "..."
                    if len(doc.page_content) > 300
                    else doc.page_content
                ),
                "score": doc.metadata.get("score", 0)
            }
        )

    return {
        "answer": answer,
        "sources": sources
    }