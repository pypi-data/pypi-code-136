from pathlib import Path
import yaml


boot_config_path = Path('/boot/wildflower-config.yml')
if boot_config_path.exists():
    with boot_config_path.open('r', encoding="utf-8") as fp:
        config = yaml.safe_load(fp.read())
else:
    config = {
        "device_id": "deadbeef",
        "assignment-id": "deadbeef",
        "environment-id": "deadbeef",
    }

DEVICE_ID = config.get("device_id", "unknown")
ASSIGNMENT_ID = config.get("assignment-id", "unknown")
ENV_ID = config.get("environment-id", "unknown")
