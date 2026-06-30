from fastapi import FastAPI

from app.api.routes.upload import router as upload_router
from app.api.routes.chat import router as chat_router

app = FastAPI(
    title="DocuTrust Ultra",
    version="1.0.0"
)

# Upload API
app.include_router(
    upload_router,
    tags=["Upload"]
)

# Chat API
app.include_router(
    chat_router,
    tags=["Chat"]
)


@app.get("/")
def root():
    return {
        "message": "DocuTrust Ultra API Running Successfully!"
    }