from __future__ import annotations
import argparse
from .log import configure_logging
from .cmd import add_command, exec_command

configure_logging()

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

add_command(subparsers, "zut.cred")
add_command(subparsers, "zut.git", name="checkversion")

if __name__ == "__main__":
    exec_command(parser)
