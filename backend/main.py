from fastapi import FastAPI

from app.config.settings import settings

from app.database import db

from app.api.v1.upload import router as upload_router


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)


app.include_router(
    upload_router,
    prefix="/api/v1",
    tags=["Upload"],
)


@app.get("/")
def root():
    return {
        "message": f"{settings.APP_NAME} Backend Running"
    }


@app.get("/health")
def health():
    try:
        db.command("ping")

        return {
            "status": "healthy",
            "database": "connected"
        }

    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e)
        }