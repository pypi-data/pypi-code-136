from dataclasses import dataclass
from typing import List

from vim_quest_cli.status import VimGlobalStatus, SpecialChar


def assign_screen_size(state: VimGlobalStatus, nb_rows: int, nb_cols: int) -> VimGlobalStatus:
    return state.copy(
        screen_cols=nb_rows,
        screen_rows=nb_cols - 1,  # Leave space for the status
    )


@dataclass(frozen=True)
class ScreenSize:
    rows: int
    cols: int


@dataclass(frozen=True)
class CursorPos:
    line: int
    col: int


@dataclass(frozen=True)
class ScreenData:
    screen_viewport: List[str]
    status_line: str
    cursor_pos: CursorPos


def get_status_line(state: VimGlobalStatus) -> str:
    return f'{state.command!r}  pos: {state.cursor_lnum},{state.cursor_colnum}'


def get_screen_viewport(state: VimGlobalStatus, unicode_supported=True) -> List[str]:
    xpos, nbcols = state.screen_xpos, state.screen_cols
    ypos, nbrows = state.screen_ypos, state.screen_rows

    x_start, x_end = xpos, xpos + nbcols
    y_start, y_end = ypos, ypos + nbrows

    relevant_lines = state.buffer[y_start: y_end]
    res = [l[x_start: x_end] for l in relevant_lines]

    if not unicode_supported:
        def _replace_unicode_line(l: str, replace_by='??'):
            return ''.join((replace_by if SpecialChar.is_emoji(c) else c) for c in l)

        res = [_replace_unicode_line(l) for l in relevant_lines]

    return res


def get_cursor_pos_on_screen(state: VimGlobalStatus) -> CursorPos:
    return CursorPos(
        line=state.cursor_lnum - state.screen_ypos - 1,
        col=state.cursor_colnum - state.screen_xpos - 1,
    )


def get_screen_data(state: VimGlobalStatus, unicode_supported=True) -> ScreenData:
    return ScreenData(
        status_line=get_status_line(state),
        screen_viewport=get_screen_viewport(state, unicode_supported),
        cursor_pos=get_cursor_pos_on_screen(state),
    )
