# First have a method that take a suite of
import dataclasses
import enum
from typing import List

# import emoji
#from emoji import EMOJI_UNICODE_ENGLISH, UNICODE_EMOJI_ALIAS_ENGLISH
EMOJI_UNICODE_ENGLISH = {
    u':brick:': u'\U0001F9F1',

}

UNICODE_EMOJI_ALIAS_ENGLISH = {v: k for k, v in EMOJI_UNICODE_ENGLISH.items()}


@dataclasses.dataclass(frozen=True)
class VimGlobalStatus:
    cursor_colnum: int = 1
    cursor_lnum: int = 1
    cursor_want: int = 1

    screen_rows: int = 2
    screen_cols: int = 2
    screen_xpos: int = 0
    screen_ypos: int = 0

    buffer: List[str] = dataclasses.field(default_factory=list)
    # paste: str = ""
    # command: str = ""
    # search: str = ""
    command: List[str] = dataclasses.field(default_factory=list)

    should_quit: bool = True

    # action: None = None  # Placeholder for any other kind of action outside the status

    def copy(self, **changes):
        return dataclasses.replace(self, **changes)

    def with_added_command(self, command: List[str]):
        return self.copy(command=self.command + command)

    allowed_commands = "ALL"


@enum.unique
class SpecialChar(enum.Enum):
    BRICKS = EMOJI_UNICODE_ENGLISH[':brick:']  # 🧱

    @staticmethod
    def is_emoji(s):
        return s in UNICODE_EMOJI_ALIAS_ENGLISH


@enum.unique
class Keys(enum.Enum):
    EXIT = 'KEY_ESC'
    RIGHT = 'KEY_RIGHT'
    LEFT = 'KEY_LEFT'
    UP = 'KEY_UP'
    DOWN = 'KEY_DOWN'


END_OF_LINE_MAX = 2147483647

# Lines to keep between the cursors and the beginning/end of the screen.
# This doesn't work if it's the actual beginning/end of the file
LINE_BUFFER = 5
