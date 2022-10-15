import logging
from typing import Optional

from timetable_cli.utils import check_colorscheme

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class ActivityCategory:
    title: str
    colorscheme: dict

    def __init__(self, title: str, colorscheme: Optional[dict]):
        if colorscheme:
            check_colorscheme(colorscheme)
        else:
            colorscheme = {}
        self.title = title
        self.colorscheme = colorscheme
