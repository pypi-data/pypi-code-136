import logging
import click

from capture.segmentparser import monitor_directory


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


@click.group()
def main():
    pass

#
# @main.command()
# def capture():
# from capture.legacy import capture_loop
#     capture_loop()
#
#
# @main.command()
# def upload():
# from capture.legacy import upload_loop
#     upload_loop()


@main.command()
@click.argument('path')
def upload_monitor(path):
    monitor_directory(path)


if __name__ == '__main__':
    main()
