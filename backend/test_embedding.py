from app.services.parser_service import parse_document
from app.services.chunk_service import chunk_documents
from app.services.embedding_service import generate_embeddings

docs = parse_document("data/uploads/Anurag_Sahu_Resume_Reliance.pdf")

chunks = chunk_documents(docs)

print("Chunks:", len(chunks))

embeddings = generate_embeddings(chunks)

print("Embeddings:", len(embeddings))
if len(embeddings) > 0:
    print("Dimension:", len(embeddings[0]))
else:
    print("No embeddings generated.")