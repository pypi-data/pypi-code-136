#!/usr/bin/env python3.8
import select
import sys
import tty

from vim_quest_cli import vim_quest_cli

def test_stdin(timeout=.5):
    fno = sys.stdin.fileno()
    tty.setraw(fno)

    res = sys.stdin.read(1)  # Blocking

    rfds, _, _ = select.select([fno], [], [], timeout)
    print(f'{rfds=!r}')
    while sys.stdin.fileno() in rfds or sys.stdin in rfds:
        res += sys.stdin.read(1)
        rfds, _, _ = select.select([sys.stdin.fileno()], [], [], 0)
        print(f'{rfds=!r}')

    return res

def main_other():
    print('starting vimquest')
    while True:
        v = test_stdin()
        print(f'{v=!r}')
        if v == 'q':
            break

def main_cli():
    print('starting vimquest')
    vim_quest_cli.main()

if __name__ == '__main__':
    main_cli()
