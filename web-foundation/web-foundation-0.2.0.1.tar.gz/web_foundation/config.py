from pathlib import Path
from typing import TypeVar

from pydantic import BaseModel, BaseSettings


class DbConfig(BaseModel):
    host: str
    port: str
    database: str
    user: str
    password: str
    db_schema: str
    with_migrations: bool
    migrations_path: Path


class AppConf(BaseSettings):
    app_name: str
    database: DbConfig


GenericConfig = TypeVar("GenericConfig", bound=BaseSettings)
