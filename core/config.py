import os
from pathlib import Path
from dotenv import load_dotenv
from typing import Optional

directory = (Path(__file__) / ".." / "..").resolve()
env = os.path.join(directory, ".env")
load_dotenv(dotenv_path=env)


class Settings:
    APP_TITLE: Optional[str] = os.getenv("APP_TITLE")
    APP_HOST: Optional[str] = os.getenv("APP_HOST")
    ROUTER_PREFIX:Optional[str] = os.getenv("ROUTER_PREFIX")


settings = Settings()
