from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    APP_NAME: str = "DocuTrust"

    APP_VERSION: str = "1.0"

    MONGODB_URI: str

    DATABASE_NAME: str

    GEMINI_API_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()