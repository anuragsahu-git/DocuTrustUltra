from app.services.parser_service import parse_document

docs = parse_document("data/uploads/ANNEXURE_VII_A.pdf")

print("Number of documents:", len(docs))

if len(docs) > 0:
    print()
    print(docs[0].page_content[:1000])