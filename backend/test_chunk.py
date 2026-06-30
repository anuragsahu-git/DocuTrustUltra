from app.services.parser_service import parse_document

docs = parse_document("data/uploads/ANNEXURE_VII_A.pdf")

print(type(docs))
print(len(docs))

if len(docs):
    print(docs[0].page_content[:500])