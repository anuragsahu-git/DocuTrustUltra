import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_answer(query: str, context: str) -> str:
    prompt = f"""
You are DocuTrust AI.

Answer ONLY using the provided context.

If the answer is not present, reply:

"I couldn't find that information in the uploaded documents."

Context:
{context}

Question:
{query}

Answer:
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text.strip()