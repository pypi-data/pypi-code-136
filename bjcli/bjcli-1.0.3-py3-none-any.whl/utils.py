import os
from pathlib import Path
from typing import Union


def create_workers(workers: int) -> Union[set[int], None]:
    pids = set()

    for i in range(workers):
        print(f'Forking worker #{i + 1}')

        pid = os.fork()

        print(f'Forked worker #{i + 1}')

        if pid > 0:
            #  On master

            pids.add(pid)
        elif pid == 0:
            #  In worker

            return None

    return pids


def set_socket_permissions(path: str) -> None:
    if path.startswith('unix:'):
        path = path[5:]

    spath = Path(path)

    spath.chmod(0o777)
