# TODO: using .executor_interface instead of full path failed when bundle.
from vim_quest_cli.executors.executor_interface import Executor
from vim_quest_cli.status import VimGlobalStatus, SpecialChar, Keys, END_OF_LINE_MAX, LINE_BUFFER


class LocalExecutor(Executor):

    def execute_command(self, state_start: VimGlobalStatus) -> VimGlobalStatus:
        state_res = self._execute_single_command(state_start)
        state_res = LocalExecutor._check_rules(state_start, state_res)

        return LocalExecutor._refresh_view(state_res)

    @staticmethod
    def _get_char_under_cursor(state: VimGlobalStatus):
        line = state.buffer[state.cursor_lnum - 1][:]
        pos = state.cursor_colnum
        while line:
            first_char, line = line[0], line[1:]
            if SpecialChar.is_emoji(first_char):
                pos -= 2
            else:
                pos -= 1
            if pos <= 0:
                return first_char
        return None

    @staticmethod
    def _check_rules(state_start, state_res):
        hey = LocalExecutor._get_char_under_cursor(state_res)
        print(hey)
        if LocalExecutor._get_char_under_cursor(state_res) == SpecialChar.BRICKS.value:
            return state_start.copy(command=state_res.command)
        return state_res

    def _execute_single_command(self, state: VimGlobalStatus) -> VimGlobalStatus:
        # First try to read numbers
        c = state.command[:]

        if c[0] == Keys.DOWN.value or c[0] == "j":
            return self._cursor_down(state.copy(command=c[1:]))

        if c[0] == Keys.UP.value or state.command[0] == "k":
            return self._cursor_up(state.copy(command=c[1:]))

        if c[0] == Keys.LEFT.value or state.command[0] == "h":
            return self._cursor_left(state.copy(command=c[1:]))

        if c[0] == Keys.RIGHT.value or state.command[0] == "l":
            return self._cursor_right(state.copy(command=c[1:]))

        if c[0] == '$':
            return self._cursor_end_of_line(state.copy(command=c[1:]))

        if c[0] == '0':
            return self._cursor_beginning_of_line(state.copy(command=c[1:]))

        if c[0] == 'G':
            return self._cursor_end_of_file(state.copy(command=c[1:]))

        if c[0:2] == ['g', 'g']:
            return self._cursor_beginning_of_file(state.copy(command=c[2:]))

        if c[-1] == Keys.EXIT.value:  # TODO: it's not specifically like that
            return state.copy(command=[])

        return state

    @staticmethod
    def _cursor_down(state: VimGlobalStatus) -> VimGlobalStatus:
        new_lnum = state.cursor_lnum + 1
        if new_lnum > len(state.buffer):
            return state
        col = min(state.cursor_want, LocalExecutor._get_line_len(state, new_lnum))
        return state.copy(cursor_lnum=new_lnum, cursor_colnum=col)

    @staticmethod
    def _cursor_up(state: VimGlobalStatus) -> VimGlobalStatus:
        new_lnum = state.cursor_lnum - 1
        if new_lnum == 0:
            return state
        col = min(state.cursor_want, LocalExecutor._get_line_len(state, new_lnum))
        return state.copy(cursor_lnum=new_lnum, cursor_colnum=col)

    @staticmethod
    def _cursor_left(state: VimGlobalStatus) -> VimGlobalStatus:
        new_col = state.cursor_colnum - 1
        if new_col == 0:
            return state
        return state.copy(cursor_colnum=new_col, cursor_want=new_col)

    @staticmethod
    def _cursor_right(state: VimGlobalStatus) -> VimGlobalStatus:
        new_col = state.cursor_colnum + 1
        if new_col > LocalExecutor._get_line_len(state):
            return state
        return state.copy(cursor_colnum=new_col, cursor_want=new_col)

    @staticmethod
    def _cursor_end_of_line(state: VimGlobalStatus) -> VimGlobalStatus:
        return state.copy(
            cursor_colnum=LocalExecutor._get_line_len(state),
            cursor_want=END_OF_LINE_MAX,
        )

    @staticmethod
    def _cursor_beginning_of_line(state: VimGlobalStatus) -> VimGlobalStatus:
        return state.copy(
            cursor_colnum=1,
            cursor_want=1,
        )

    @staticmethod
    def _cursor_end_of_file(state: VimGlobalStatus) -> VimGlobalStatus:
        # TODO : It starts at the first non-space character.
        return state.copy(
            cursor_want=1,
            cursor_colnum=1,
            cursor_lnum=len(state.buffer) - 1
        )

    @staticmethod
    def _cursor_beginning_of_file(state: VimGlobalStatus) -> VimGlobalStatus:
        return state.copy(
            cursor_want=1,
            cursor_colnum=1,
            cursor_lnum=1,
        )

    @staticmethod
    def _get_line_len(state, lnum=None, min_1=True):
        lnum = state.cursor_lnum if lnum is None else lnum
        line_len = len(state.buffer[lnum - 1])
        if min_1:
            line_len = max(line_len, 1)
        return line_len

    @staticmethod
    def _refresh_view(state):
        cursor_y = state.cursor_lnum

        # Find the max and min of the view, count the lines buffers and absolute min max
        max_view = min(cursor_y - 1 - LINE_BUFFER, len(state.buffer) - state.screen_rows - 1)
        min_view = max(cursor_y - state.screen_rows + LINE_BUFFER, 0)

        # If the view is inside
        if state.screen_ypos <= min_view:
            return state.copy(screen_ypos=min_view)

        if state.screen_ypos >= max_view:
            return state.copy(screen_ypos=max_view)

        return state
