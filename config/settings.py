import pathlib
from functools import lru_cache

__all__ = ["settings"]
PROJECT_BASE_DIR = pathlib.Path(__file__).resolve().parent.parent


class Settings:

    DEBUG: bool = False
    MONGO_DB_NAME: str = "vimmi"
    MONGO_URL: str = "mongodb://127.0.0.1:27017/"
    BASE_DIR: pathlib.Path = PROJECT_BASE_DIR

    class Config:
        env_file = PROJECT_BASE_DIR / ".env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()
