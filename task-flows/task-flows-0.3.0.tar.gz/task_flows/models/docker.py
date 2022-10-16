from typing import Dict, Optional, Sequence, Union

from dotenv import dotenv_values
from pydantic import BaseModel, FilePath, validator


class Volume(BaseModel):
    """Docker volume."""

    host_path: str
    container_path: str
    read_only: bool = True


class Ulimit(BaseModel):
    name: str
    soft: Optional[int] = None
    hard: Optional[int] = None

    @validator("soft", always=True)
    def check_has_limit(cls, soft, values):
        if soft is None and values.get("hard") is None:
            raise ValueError("Either `soft` limit or `hard` limit must be set.")


class Container(BaseModel):
    image: str
    command: str
    network_mode: str = "host"
    init: bool = True
    user: Optional[str] = None
    mem_limit: Optional[str] = None
    shm_size: Optional[str] = None
    env: Optional[Dict[str, str]] = None
    env_file: Optional[FilePath] = None
    volumes: Optional[Union[Volume, Sequence[Volume]]] = None
    ulimits: Optional[Union[Ulimit, Sequence[Ulimit]]] = None

    @validator("env_file")
    def load_env_file(cls, f):
        if f is not None:
            return dotenv_values(f)

    @validator("volumes", "ulimits")
    def check_iterable(cls, v):
        if not isinstance(v, (list, tuple, set)):
            return [v]
        return v
