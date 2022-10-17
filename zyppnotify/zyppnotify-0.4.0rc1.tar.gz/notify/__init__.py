import logging

from notify.mail import NotifyMail  # noqa
from notify.teams import NotifyTeams  # noqa
from notify.utils import dataframe_to_html, format_numbers  # noqa

logging.basicConfig(
    format="%(asctime)s.%(msecs)03d [%(levelname)-5s] [%(name)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)

name = "notify"
__version__ = "0.4.0-rc.1"
