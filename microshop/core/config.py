from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/shop.db"
    db_echo: bool = False


settings = Settings()
