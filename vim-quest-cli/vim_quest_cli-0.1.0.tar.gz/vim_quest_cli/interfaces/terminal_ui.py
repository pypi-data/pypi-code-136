from vim_quest_cli.executors.executor_interface import Executor
from vim_quest_cli.interfaces.common import get_screen_data
from vim_quest_cli.status import VimGlobalStatus


class TerminalUI:

    def __init__(self, executor: Executor, state: VimGlobalStatus, unicode_supported=True):
        self._executor: Executor = executor
        self._state: VimGlobalStatus = state
        self._unicode_supported = unicode_supported
        self._screen_size_has_been_initialized = False

    def _assure_screen_size_present(self, stdscr):
        if self._screen_size_has_been_initialized:
            return
        self._screen_size_has_been_initialized = True
        screen_rows, screen_cols = stdscr.getmaxyx()
        self._state = self._state.copy(
            screen_cols=screen_cols,
            screen_rows=screen_rows - 1,  # Leave space for the status
        )

    def loop_one_step(self, input_str, stdscr):
        self._assure_screen_size_present(stdscr)

        if input_str is None:
            self._refresh_state(stdscr)
            return

        if input_str == '\x1b':
            input_str = 'KEY_ESC'

        if input_str in ('Z', 'z', 'q'):  # Just to be sure to have an exit
            raise StopIteration()

        if input_str is not None:
            self._state = self._executor.execute_command(self._state.with_added_command([input_str]))

        self._refresh_state(stdscr)

    def _clean_before_leaving(self, stdscr):
        stdscr.clear()
        stdscr.move(0, 0)
        stdscr.refresh()

    def start_with_window(self, stdscr):

        try:
            self.loop_one_step(None, stdscr)
            while True:
                input_str = stdscr.getkey()
                self.loop_one_step(input_str, stdscr)
        except StopIteration:
            self._clean_before_leaving(stdscr)
            return

    def start(self):
        __import__('curses').wrapper(self.start_with_window)

    def _refresh_state(self, stdscr):
        stdscr.clear()

        screen_data = get_screen_data(self._state, self._unicode_supported)

        to_show = '\n'.join(screen_data.screen_viewport)

        stdscr.addstr(0, 0, to_show)

        stdscr.addstr(self._state.screen_rows, 0, f'{screen_data.status_line}')

        stdscr.move(screen_data.cursor_pos.line, screen_data.cursor_pos.col)

        stdscr.refresh()
