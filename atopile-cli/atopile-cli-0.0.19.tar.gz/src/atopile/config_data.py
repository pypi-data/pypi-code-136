from . import options
import yaml

def load_config_data():
    config_path = options.atopile_file.value
    try: 
        with config_path.open() as f:
            config_data = yaml.safe_load(f)
    except FileNotFoundError:
        config_data = {}

    return config_data

def save_config_data(config_data):
    config_path = options.atopile_file.value
    with config_path.open('w') as f:
        yaml.safe_dump(config_data, f)
