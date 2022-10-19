import os
import sys
import signal
import ipaddress
import importlib

import bjoern  # Does not work for Windows

from . import parser, utils

DEFAULT_PORT: int = 8088


def main():
    args = parser.parse_args()

    if args.workers < 1:
        raise AttributeError('Workers must not be less than 1')

    sys.path.insert(1, os.getcwd())

    full_module_path = args.positional[0]

    try:
        module_path, attr = full_module_path.split(':')
    except ValueError:
        raise AttributeError(
            f'No module attribute specified in "{full_module_path}"'
        )

    if not attr:
        raise AttributeError(
            f'Module attribute cannot be empty ({full_module_path})')

    module = importlib.import_module(module_path)

    app = getattr(module, attr)

    workers = args.workers

    host = args.host

    port = args.port

    if not port:
        try:
            ipaddress.ip_network(host)

            port = DEFAULT_PORT
        except ValueError:
            pass

    print(f'Starting Bjoern on {host}{f":{port}" if port else ""}')

    bjoern.listen(app, host, port)

    print('Bjoern server has started')

    if not port:
        utils.set_socket_permissions(host)

    pids = utils.create_workers(workers)

    if not pids:
        try:
            bjoern.run()
        except FileNotFoundError as e:
            print(e)
        except KeyboardInterrupt:
            pass

        exit()

    try:
        # Wait for the first worker to exit. They should never exit!
        # Once first is dead, kill the others and exit with error code.

        pid, _ = os.wait()

        pids.remove(pid)

    finally:
        for pid in pids:
            os.kill(pid, signal.SIGINT)

            exit(1)


if __name__ == '__main__':
    main()
