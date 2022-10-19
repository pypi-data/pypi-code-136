import collections.abc
import logging
from hashlib import sha1
from pathlib import Path
from typing import List

import attrs
from termcolor import colored

from . import options


def add_obj_to_hash(obj, hash):
    if hasattr(obj, '__attrs_attrs__'):
        attrs_to_hash = [a.name for a in obj.__attrs_attrs__]
        values_to_hash = [attrs.asdict(obj)[k] for k in attrs_to_hash]
    elif isinstance(obj, dict):
        attrs_to_hash = list(obj.keys())
        values_to_hash = [obj[k] for k in attrs_to_hash]
    elif isinstance(obj, list):
        values_to_hash = obj
    else:
        values_to_hash = [str(obj)]

    for value in values_to_hash:
        if isinstance(value, str):
            hash.update(value.encode())
        else:
            add_obj_to_hash(value, hash)

def compute_object_hash(obj) -> str:
    hash = sha1()
    add_obj_to_hash(obj)
    return hash.hexdigest()

def add_file_to_hash(path: Path, hash):
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash.update(chunk)

def hash_file(path: Path) -> str:
    hash = sha1()
    add_file_to_hash(path, hash)
    return hash.hexdigest()

class SubLog(logging.Handler):
    """
    A log that stores items in a list
    """

    terminator = '\n'

    def __init__(self, name: str, level: int = logging.DEBUG) -> None:
        super().__init__(level)
        self.log: List[logging.LogRecord] = []
        self.name = name
        self.logger = logging.Logger(name)
        self.logger.addHandler(self)
        self.strictness = logging.WARNING

    @staticmethod
    def _map_color(levelno: int):
        if levelno <= logging.DEBUG:
            return 'white'
        if levelno <= logging.INFO:
            return 'blue'
        if levelno <= logging.WARNING:
            return 'yellow'
        return 'red'

    @classmethod
    def _colorized_level(cls, levelno: int):
        return colored(logging.getLevelName(levelno), cls._map_color(levelno))

    def _header(self) -> str:
        msg = f'=== {self.name} logs === \n'
        colorized_level = self._colorized_level(self.max_levelno)
        msg += f'status: {colorized_level}\n'
        msg += f'\n'
        return msg

    def chronological(self) -> str:
        msg = self.header()
        for record in self.log:
            msg += self.format(record) + self.terminator
        return msg

    def __str__(self) -> str:
        msg = self._header()
        for record in self.prioritised():
            msg += self.format(record) + self.terminator
        return msg
    
    def __bool__(self):
        return self.max_levelno <= self.strictness  

    def emit(self, record):
        self.log.append(record)

    def format(self, record: logging.LogRecord):
        level = self._colorized_level(record.levelno)
        return f'{level}::{record.name}:{record.msg}'

    def prioritised(self):
        return sorted(self.log, key=lambda r: r.levelno, reverse=True)

    def show(self):
        print(str(self))

    def get_logger(self, logger_name: str) -> logging.Logger:
        logger = logging.Logger(logger_name)
        logger.parent = self.logger
        logger.addHandler(self)
        return logger

    def debug(self, *args, **kwargs):
        self.logger.debug(*args, **kwargs)

    def info(self, *args, **kwargs):
        self.logger.info(*args, **kwargs)

    def warning(self, *args, **kwargs):
        self.logger.warning(*args, **kwargs)

    def error(self, *args, **kwargs):
        self.logger.error(*args, **kwargs)

    def fatal(self, *args, **kwargs):
        self.logger.fatal(*args, **kwargs)
    
    @property
    def max_levelno(self) -> int:
        if self.log:
            return max(r.levelno for r in self.log)
        else: 
            return logging.NOTSET

class AtopileError(Exception):
    """
    Represents something wrong with the data fed in
    """
    pass

def merge_dict(d, u):
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = merge_dict(d.get(k, {}), v)
        else:
            d[k] = v
    return d

def reindent_str(string: str, indent=0) -> str:
    indent = ' ' * indent
    reindented = indent + f'\n{indent}'.join([v.strip() for v in string.splitlines()])
    return reindented

def resolve_project_relative_ref(ref):
    """
    Figure out what the user means when they specify a reference to something within some project
    """
    # let's first assume this is an absolute path
    # if an absolute reference is provided, we're assuming it's in the project, obviously
    # in this case we should be able to say we can work out the project root based on it
    path = Path(ref).absolute()
    if path.exists():
        options.project_dir.set_value(path, options.Level.CLICK_OPTION)
        return path.relative_to(options.project_dir.value)

    # if it's not an absolute path, we're assuming it's a relative path with respect to the project root
    path = options.project_dir.value / ref
    if path.exists():
        return path.relative_to(options.project_dir.value)

    # okay, I dunno what you're talking about
    raise FileNotFoundError
