from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    ENVIRONMENT: str

    MONGODB_URI: str
    DATABASE_NAME: str

    CHROMA_DB_PATH: str

    OPENAI_API_KEY: str = ""
    LANGSMITH_API_KEY: str = ""
    GEMINI_API_KEY: str = ""

    SECRET_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()