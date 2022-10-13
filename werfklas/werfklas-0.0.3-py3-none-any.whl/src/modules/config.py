
import yaml
from pathlib import Path

ROOT_DIR = Path(__file__).parents[2]

def load_config():
    with open(f"{ROOT_DIR}/cfg/config.yml", "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    return cfg
