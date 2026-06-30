import google.generativeai as genai

from app.config.settings import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_answer(question: str, context: str):

    prompt = f"""
You are DocuTrust Ultra, an enterprise AI document assistant.

Rules:
- Answer ONLY from the provided context.
- Never make up facts.
- If the answer is missing, reply exactly:
"I couldn't find that information in the uploaded documents."
- Be concise and professional.
- Use bullet points where appropriate.

Context:
{context}

Question:
{question}

Answer:
"""

    response = model.generate_content(prompt)

    return response.text