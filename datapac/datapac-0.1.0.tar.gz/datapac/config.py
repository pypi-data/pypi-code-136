import os
from typing import Literal

from pydantic import BaseSettings

app_env = os.environ.get("APP_ENV", "dev")


class Settings(BaseSettings):
    app_env: Literal["production", "staging", "dev", "test"] = "dev"
    log_level: Literal["ERROR", "WARNING", "INFO", "DEBUG"] = "WARNING"


settings = Settings()
