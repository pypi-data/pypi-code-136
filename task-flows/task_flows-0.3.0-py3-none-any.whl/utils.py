import os
from functools import lru_cache
from pathlib import Path
from subprocess import run

import sqlalchemy as sa
from pydantic import BaseSettings
from ready_logger import get_logger
from sqlalchemy.engine import Engine

logger = get_logger("task-flows")
systemd_dir = Path.home() / ".config/systemd/user"


@lru_cache(maxsize=None)
def get_engine(var_name="POSTGRES_URL") -> Engine:
    """Create an Sqlalchemy engine using a Postgresql URL from environment variable."""
    if not (url := os.getenv(var_name)):
        raise RuntimeError(
            f"Environment variable {var_name} is not set. Can not connect to database."
        )
    return sa.create_engine(url)


def systemctl(*args):
    run(["systemctl", "--user", *args])


class AlertSettings(BaseSettings):
    # Send alerts to Slack on selected events.
    alert_slack: bool = False
    # Send email alerts on selected events.
    alert_email: bool = False
    # Send alerts when task starts.
    alert_on_start: bool = False
    # Send alert on task error.
    alert_on_error: bool = False
    # Send alert when task is finished.
    alert_on_finish: bool = False

    class Config:
        env_prefix = "task_flows_"
