from pydantic import AnyUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: AnyUrl = "postgresql+asyncpg://postgres:123456@localhost:5432/litestar"
    # app_host: str = "0.0.0.0"
    app_host: str = "localhost"
    app_port: int = 5000
    environment: str = "development"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
