import json
from pathlib import Path


__all__ = ['version_info']

BASE_DIR = Path(__file__).resolve().parent

version_info = json.load(BASE_DIR.joinpath('version', 'version.json').open())
