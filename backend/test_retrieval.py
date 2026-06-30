from app.services.retrieval_service import retrieve_documents

query = "What programming languages does Anurag know?"

results = retrieve_documents(query)

print("=" * 60)
print("QUERY:")
print(query)

print("\nTOP RESULT:\n")

for i, doc in enumerate(results["documents"][0], start=1):
    print(f"Result {i}")
    print("-" * 40)
    print(doc)
    print()