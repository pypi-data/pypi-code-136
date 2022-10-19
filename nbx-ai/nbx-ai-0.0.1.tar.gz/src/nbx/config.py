import os
from pathlib import Path

from nbx.util import load_json, set_json_value, load_json_value

DEFAULT_NOTES_DIR = Path(Path.home(), ".nbx/notes")


def load_config():
    # default config
    config = {
        "notes_dir": DEFAULT_NOTES_DIR,
        "search_method": "regex"
    }
    config_file = Path(Path.home(), ".nbx/config.json")
    if config_file.exists():
        config.update(load_json(config_file))
    return config


def set_notes_dir(notes_dir: Path):
    # write to the configuration
    config_dir = Path(Path.home(), ".nbx")
    if not config_dir.exists():
        config_dir.mkdir(parents=True)
    config_file = Path(config_dir, "config.json")
    config_file.touch(exist_ok=True)
    set_json_value(config_file, "notes_dir", os.fspath(notes_dir))


def set_search_method(method: str):
    config_dir = Path(Path.home(), ".nbx")
    if not config_dir.exists():
        config_dir.mkdir(parents=True)
    config_file = Path(config_dir, "config.json")
    set_json_value(config_file, "search_method", method)


def set_openai_token(token: str):
    config_dir = Path(Path.home(), ".nbx")
    if not config_dir.exists():
        config_dir.mkdir(parents=True)
    config_file = Path(config_dir, "config.json")
    set_json_value(config_file, "openai_token", token)


def set_pinecone_token(token: str):
    config_dir = Path(Path.home(), ".nbx")
    if not config_dir.exists():
        config_dir.mkdir(parents=True)
    config_file = Path(config_dir, "config.json")
    set_json_value(config_file, "pinecone_token", token)


def load_pinecone_token() -> str:
    config_dir = Path(Path.home(), ".nbx")
    if not config_dir.exists():
        return ""
    config_file = Path(config_dir, "config.json")
    return load_json_value(config_file, "pinecone_token", "")
