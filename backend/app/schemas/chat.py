from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str


class Source(BaseModel):
    document: str
    page: int
    chunk: str
    score: float


class ChatResponse(BaseModel):
    answer: str
    sources: list[Source]