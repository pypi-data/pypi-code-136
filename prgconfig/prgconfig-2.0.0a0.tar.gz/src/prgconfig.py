# Copyright 2020-2022 Rémy Taymans <remytms@tsmail.eu>
# License GPL-3.0 or later (https://www.gnu.org/licenses/gpl.html).

"""Configuration manager using toml language for configuration files."""

import platform
from collections import UserDict
from os import environ
from pathlib import Path

import tomlkit

__productname__ = "prgconfig"
__version__ = "2.0.0-alpha.0"
__license__ = "GPL-3.0-or-later"


class PrgConfig(UserDict):
    """Handel configuration of a program"""

    def __init__(
        self,
        prg_name,
        file_ext=None,
        defaults_file=None,
        config_file_path=None,
        merge=True,
    ):
        """
        Create a PrgConfig. It will not loads the configuration files.
        To load configuration file use the `load()` method.

        :param prg_name: name of the program used to determine
        configuration file name and configuration file location.
        :type prg_name: str

        :param file_ext: extention added to the configuration file name.
        :type file_ext: [str]

        :param defaults_file: path to a file containing a default
        configuration.
        :type defaults_file: str or Path

        :param config_file_path: list of path of the configuration files
        the first is the most important, the last is the less important.
        This implies that, if an element is present in several files,
        the first one found is taken into account the others are
        ignored.
        :type config_files: [str] or [Path]

        :param merge: Merge all configuration file found in
        :type merge: bool
        """
        super().__init__()  # UserDict constructor
        # XDG environment variable as Path and list of Path
        self.xdg_config_home = Path(
            environ.get("XDG_CONFIG_HOME", Path.home() / ".config")
        )
        self.xdg_config_dirs = [
            Path(path)
            for path in environ.get("XDG_CONFIG_DIRS", "").split(":")
            if path
        ] or [Path("/etc", "xdg")]
        self.windows_dir = Path(
            environ.get("APPDATA", Path.home() / "AppData/Roaming")
        )
        self.macos_dir = Path.home() / "Library/Application Support"
        self.prg_name = prg_name
        self.file_ext = [".conf", ".toml"] if file_ext is None else file_ext
        self.defaults_file = defaults_file
        # Config file path
        if config_file_path is not None:
            self.config_file_path = config_file_path
        else:
            self.config_file_path = self.default_config_file_path
        self.merge = merge
        self.config_sources = None
        self.data = None

    @staticmethod
    def getplatform():
        """Return the OS system beeing used"""
        return platform.system()

    @property
    def config_file_path(self):
        """Return config_file_path which is a list"""
        return self._config_file_path

    @config_file_path.setter
    def config_file_path(self, value):
        """Value can be str, Path or an iterable containing str or Path"""
        if isinstance(value, (str, Path)):
            self._config_file_path = [Path(value)]
        else:
            self._config_file_path = [Path(path) for path in value]

    @property
    def default_config_file_path(self):
        """Return a list of files to look for configuration."""
        config_files = []
        config_file_names = [self.prg_name + ext for ext in self.file_ext]

        # In current directory
        # <prg_name>{file_ext}
        config_files += [Path(name) for name in config_file_names]

        # In current directory hidden file
        # .<prg_name>{file_ext}
        config_files += [Path("." + name) for name in config_file_names]

        # Windows directory
        if self.getplatform() == "Windows":
            config_files += [
                self.windows_dir / name for name in config_file_names
            ]
            config_files += [
                self.windows_dir / self.prg_name / name
                for name in config_file_names
            ]
            return config_files

        # For MacOs
        if self.getplatform() == "Darwin":
            config_files += [
                self.macos_dir / name for name in config_file_names
            ]
            config_files += [
                self.macos_dir / self.prg_name / name
                for name in config_file_names
            ]

        # In xdg_config_home
        # $XDG_CONFIG_HOME/<prg_name>{file_ext}
        config_files += [
            self.xdg_config_home / name for name in config_file_names
        ]
        # $XDG_CONFIG_HOME/<prg_name>/config
        config_files += [self.xdg_config_home / self.prg_name / "config"]
        # $XDG_CONFIG_HOME/<prg_name>/<prg_name>{file_ext}
        config_files += [
            self.xdg_config_home / self.prg_name / name
            for name in config_file_names
        ]

        # In home
        # $HOME/.<prg_name>{file_ext}
        config_files += [
            Path.home() / ("." + name) for name in config_file_names
        ]

        # In xdg_config_dirs
        for xdg_dir in self.xdg_config_dirs:
            # $XDG_CONFIG_DIRS/<prg_name>{file_ext}
            config_files += [xdg_dir / name for name in config_file_names]
            # $XDG_CONFIG_DIRS/<prg_name>/config
            config_files += [xdg_dir / self.prg_name / "config"]
            # $XDG_CONFIG_DIRS/<prg_name>/<prg_name>{file_ext}
            config_files += [
                xdg_dir / self.prg_name / name for name in config_file_names
            ]

        # In /etc
        # /etc/<prg_name>{file_ext}
        config_files += [Path("/etc") / name for name in config_file_names]
        # /etc/<prg_name>/config
        config_files += [Path("/etc") / self.prg_name / "config"]
        # /etc/<prg_name>/<prg_name>{file_ext}
        config_files += [
            Path("/etc") / self.prg_name / name for name in config_file_names
        ]

        return config_files

    def getcheck(self, *keys, vtype=None, default=None):
        """
        Get an element and check its type.
        Giving multiple keys is like accessing sub keys.
        Return default if keys does not exists.
        Raise TypeError if value is not of type vtype.
        E.g.:
            conf.getcheck("section", "key1", vtype=str)
            It access to conf["section"]["key1"] and check that the
            value is of type str if not it raises an TypeError.

        :param keys: key to access to as multiple arguments
        :type keys: str, str,...
        :param vtype: the type of the value
        :type vtype: *
        :param default: the fallback value if the keys are not found
        :type default: *
        """
        if len(keys) < 1:
            raise TypeError(
                "getcheck() take at least 1 key as arguments. 0 given."
            )
        value = self
        for key in keys:
            try:
                value = value[key]
            except KeyError:
                value = default
                break
        if vtype is not None and not isinstance(value, vtype):
            raise TypeError(
                f"Wrong type for value of key '{keys}' in configuration file. "
                f"Received {type(value)} expecting {vtype}."
            )
        return value

    def clear(self):
        """Clear all data loaded."""
        super().clear()
        self.config_sources = None

    def dumps(self):
        """Dump configuration to a string"""
        return tomlkit.dumps(self.data)

    def load(self):
        """Loads defaults and configurations files"""
        self.data = tomlkit.TOMLDocument()
        self.config_sources = []
        # Load defaults
        self._load_defaults()
        # Resolve config files
        full_config_file_path = [
            Path(p).expanduser().resolve()
            for p in self.config_file_path
            if Path(p).expanduser().exists()
        ]
        # If merge is true, order of the config file path should be
        # reversed because it's the latest value that will be kept.
        full_config_file_path = (
            reversed(full_config_file_path)
            if self.merge
            else full_config_file_path
        )
        # Load config file
        for path in full_config_file_path:
            with path.open() as file:
                try:
                    self.update(tomlkit.load(file))
                    self.config_sources.insert(0, path)
                    if not self.merge:
                        break
                except tomlkit.exceptions.ParseError as err:
                    raise ParseError(str(err), file) from err

    def _load_defaults(self):
        """
        Load defaults_file if provided.
        self.data shoud be already initialised.
        """
        defaults_file_path = (
            Path(self.defaults_file).expanduser()
            if self.defaults_file
            else None
        )
        if defaults_file_path and defaults_file_path.exists():
            with defaults_file_path.open() as file:
                try:
                    self.update(tomlkit.load(file))
                except tomlkit.exceptions.ParseError as err:
                    raise ParseError(str(err), defaults_file_path) from err


class ConfigError(Exception):
    """General Error for this module"""


class ParseError(ConfigError):
    """Error when parsing a config file."""

    def __init__(self, message, filepath):
        """
        :param message: the message of the TomlDecodeError
        :type message: str
        :param filepath: the path to the file that generate exception
        :type filepath: Path or str
        """
        super().__init__(f"In {filepath}: {message}")
        self.filepath = filepath
