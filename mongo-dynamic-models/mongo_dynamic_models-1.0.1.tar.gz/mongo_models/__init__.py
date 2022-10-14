import json
from pathlib import Path

from mongo_models.core import MongoModels


BASE_DIR = Path(__file__).resolve().parent

version_info = json.load(BASE_DIR.joinpath('version', 'version.json').open())

__version__ = version_info['version']
