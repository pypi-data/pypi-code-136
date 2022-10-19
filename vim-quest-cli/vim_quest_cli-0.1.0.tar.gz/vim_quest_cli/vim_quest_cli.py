from vim_quest_cli.corpus import BLOCK_TEXT
from vim_quest_cli.executors.local_executor import LocalExecutor
from vim_quest_cli.interfaces.curses_window import Window
from vim_quest_cli.interfaces.terminal_ui import TerminalUI
from vim_quest_cli.status import VimGlobalStatus


def main():
    state = VimGlobalStatus(buffer=BLOCK_TEXT)
    executor = LocalExecutor()

    t = TerminalUI(executor, state, False)

    use_ansi = True

    if use_ansi:
        t.start_with_window(Window())
    else:
        t.start()


def as_single_method():
    state = VimGlobalStatus(buffer=BLOCK_TEXT)
    executor = LocalExecutor()

    t = TerminalUI(executor, state, True)

    def res_method(input: str) -> str:
        res = []
        w = Window(stdout_write_fct=res.append)
        t.loop_one_step(input, w)

        return ''.join(res)

    return res_method
