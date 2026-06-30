from app.services.llm_service import generate_answer

context = """
Python
Java
C#
Machine Learning
Deep Learning
"""

query = "What programming languages are listed?"

answer = generate_answer(query, context)

print(answer)