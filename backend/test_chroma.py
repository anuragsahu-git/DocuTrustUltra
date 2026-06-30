from uuid import uuid4

from app.services.parser_service import parse_document
from app.services.chunk_service import chunk_documents
from app.services.embedding_service import store_embeddings

docs = parse_document("data/uploads/Anurag_Sahu_Resume_Reliance.pdf")

chunks = chunk_documents(docs)

count = store_embeddings(str(uuid4()), chunks)

print("Stored:", count)