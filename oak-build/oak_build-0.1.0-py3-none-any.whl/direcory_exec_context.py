import sys
from pathlib import Path


class DirectoryExecContext:
    def __init__(self, dir: Path):
        self.dir = dir.resolve().absolute()

    def __enter__(self):
        sys.path = [str(self.dir)] + sys.path

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.path = sys.path[1:]
