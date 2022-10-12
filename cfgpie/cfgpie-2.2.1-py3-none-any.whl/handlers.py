# -*- coding: UTF-8 -*-

from ast import literal_eval
from configparser import ExtendedInterpolation, ConfigParser
from os.path import isfile, exists, realpath
from sys import argv
from typing import Iterator, Sequence, Union, List, Tuple, Dict
from decimal import Decimal
from customlib.filehandlers import FileHandler

from .constants import Key, Value, ROOT, CONFIG
from .exceptions import ArgParseError
from .utils import ensure_folder, folder, file


class ArgsParser(object):

    @staticmethod
    def _update_params(params: dict, section: str, option: str, value: str):

        if section not in params:
            params.update({section: {option: value}})
        else:
            params.get(section).update({option: value})

    @classmethod
    def parse(cls, args: Iterator[str]) -> dict:
        temp = dict()

        for arg in args:
            if arg.startswith("--") is True:
                stripped = arg.strip("-")
                try:
                    section, option = stripped.split("-")
                except ValueError:
                    raise ArgParseError(f"Inconsistency in cmd-line parameters '{arg}'!")
                else:
                    try:
                        value = next(args)
                    except StopIteration:
                        raise ArgParseError(f"Missing value for parameter '{arg}'")
                    else:
                        if value.startswith("--") is False:
                            cls._update_params(temp, section.upper(), option, value)
                        else:
                            raise ArgParseError(f"Incorrect value '{value}' for parameter '{arg}'!")
            else:
                raise ArgParseError(f"Inconsistency in cmd-line parameters '{arg}'!")

        return temp


class CfgParser(ConfigParser, ArgsParser):
    """Configuration handle."""

    _DEFAULT_CONVERTERS: dict = {
        "decimal": Decimal,
        "list": literal_eval,
        "tuple": literal_eval,
        "set": literal_eval,
        "dict": literal_eval,
        "path": realpath,
        "folder": folder,
        "file": file,
    }

    _DEFAULTS: dict = {
        "directory": ROOT,
    }

    @staticmethod
    def _as_dict(mapping: Union[Dict, List[Tuple[Key, Value]]] = None, **kwargs) -> dict:
        if isinstance(mapping, list):
            mapping = dict(mapping)

        elif mapping is None:
            mapping = dict()

        if len(kwargs) > 0:
            mapping.update(kwargs)

        return mapping

    @staticmethod
    def _exists(item: str) -> bool:
        return exists(item) and isfile(item)

    def __init__(self, **kwargs):
        super(CfgParser, self).__init__(**self._default_params(kwargs))

    def parse(self, args: Sequence[str] = None):
        """Parse command-line arguments and update the configuration."""
        if args is None:
            args = argv[1:]

        if len(args) > 0:
            self.read_dict(
                dictionary=super(CfgParser, self).parse(iter(args)),
                source="<cmd-line>"
            )

    def set_defaults(self, mapping: Union[Dict, List[Tuple[Key, Value]]] = None, **kwargs):
        """Update `DEFAULT` section with `mapping` & `kwargs`."""
        kwargs: dict = self._as_dict(mapping, **kwargs)

        if len(kwargs) > 0:
            self._read_defaults(kwargs)

    def open(self, file_path: Union[str, List[str]], encoding: str = "UTF-8", fallback: dict = None):
        """
        Read from configuration `file_path` which can also be a list of files paths.
        If `file_path` does not exist and `fallback` is provided
        the latter will be used and a new configuration file will be written.
        """

        if isinstance(file_path, str):
            file_path = [file_path]

        if any([self._exists(item) for item in file_path]):
            self.read(file_path, encoding=encoding)

        elif fallback is not None:
            self.read_dict(dictionary=fallback, source="<backup>")
            self.save(CONFIG, encoding)

    def save(self, file_path: str, encoding: str):
        """Save the configuration to `file_path`."""
        ensure_folder(file_path)
        with FileHandler(file_path, "w", encoding=encoding) as fh:
            self.write(fh)

    def _default_params(self, kwargs: dict) -> dict:
        temp: dict = kwargs.copy()
        kwargs.update(
            defaults=temp.pop("defaults", self._DEFAULTS),
            interpolation=temp.pop("interpolation", ExtendedInterpolation()),
            converters=self._get_converters(temp),
        )
        return kwargs

    def _get_converters(self, kwargs: dict) -> dict:
        if "converters" in kwargs:
            return self._merge_converters(**kwargs.pop("converters"))
        return self._DEFAULT_CONVERTERS

    def _merge_converters(self, **kwargs) -> dict:
        converters: dict = self._DEFAULT_CONVERTERS.copy()
        converters.update(**kwargs)
        return converters
