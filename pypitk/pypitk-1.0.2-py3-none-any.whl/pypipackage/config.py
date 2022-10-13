import osiotk as os
import sys as _sys
from dataclasses import dataclass, field, asdict


@dataclass(frozen=True, order=True)
class _SystemArg:

    index: int = field(init=True)
    arg: str = field(init=True)

    @property
    def argname(self):
        return self.arg.split("=", 1)[0] if "=" in self.arg else ""

    @property
    def argvalue(self):
        return self.arg.split("=", 1)[1] if "=" in self.arg else self.arg


class _SystemArgs(list[_SystemArg]):
    def __contains__(self, __key: str):
        for arg in self:
            if arg.argname == __key:
                result = True
                break
        else:
            result = False
        return result

    def __getitem__(self, __key: str | int):
        if isinstance(__key, str):
            for arg in iter(self):
                if arg.argname == __key:
                    result = arg
                    break
            else:
                result = None
        else:
            result = list.__getitem__(self, __key)
        return result

    def __delitem__(self, __key: str | int):
        if isinstance(__key, str):
            other = self.copy()
            for (i, arg) in enumerate(iter(other)):
                if arg.argname == __key:
                    list.__delitem__(self, i)
                    break

        else:
            list.__delitem__(self, __key)

    def getstr(self, __key: str) -> (str | None):
        result = self[__key]
        return None if result is None else str(result.argvalue)


def _system_args():
    return _SystemArgs(
        _SystemArg(index=index, arg=arg) for (index, arg) in enumerate(_sys.argv)
    )


@dataclass(frozen=False, order=True)
class Config:

    package_name: str = field(init=True)
    package_dir: str = field(init=True)
    pypi_username: str = field(init=True)
    pypi_password: str = field(init=True)
    pypi_email: str = field(init=True)
    package_version: str = field(init=True)
    package_description: str = field(init=True)
    python_version: str = field(init=True)
    license: str = field(init=True)
    autoinstall: bool = field(init=True)

    def __post_init__(self):
        autoinstall = self.autoinstall
        if isinstance(autoinstall,str):
            self.autoinstall = autoinstall.lower().strip() in ("t","tr","tru","true")

    def __getitem__(self, key):
        return getattr(self, key)

    def __contains__(self, key):
        return True if self[key] else False

    def __setitem__(self, __key, value):
        setattr(self, __key, value)

    def items(self):
        return asdict(self).items()

    @classmethod
    def fields(cls):
        return tuple(cls.__dataclass_fields__.keys())


__config_defaults = {
    "package_name": "pypi_package_defaultname",
    "package_dir": "/documents/pypi_packages/",
    "pypi_username": "pypi_username",
    "pypi_password": "pypi_password",
    "pypi_email": "pypi_email",
    "package_version": "1.0.0",
    "package_description": "package_description",
    "python_version": "3.7",
    "license": "MIT",
    "autoinstall":"false"
}


def __read_config_file(__path: str):
    kwargs = {}
    config_text = os.reads(__path, is_abspath=True)
    for line in (
        line for line in config_text.splitlines(keepends=False) if "=" in line
    ):
        parts = line.split("=", 1)
        k, v = parts[0], parts[1]
        kwargs[k] = v
    for config_key in Config.fields():
        if not config_key in kwargs:
            kwargs[config_key] = __config_defaults.get(config_key)
    return kwargs


def __load_config(system_args, config: dict = {}):
    for config_key in Config.fields():
        if not config_key in config:
            if system_args[config_key] is None:
                value = __config_defaults[config_key]
                message = f"Enter value for {config_key}:: (default_value = {value})\n:"
                user_value = input(message)
                if user_value:
                    value = user_value
                config[config_key] = value
    return config


def __approve_config(config: dict):
    response_str = "\n".join(f"    {k}:{v}" for k, v in config.items())
    message = f"\nBuilding package with config:\n\n{response_str}\n\ncontinue? (y/n)\n:"
    approved = input(message).lower()
    config = config if approved == "y" else None


def init_config():
    config = {}
    system_args = _system_args()
    config_path = system_args.getstr("config_path")
    if config_path is not None:
        config = __read_config_file(config_path)
        del system_args["config_path"]
    else:
        __load_config(system_args=system_args, config=config)
    __approve_config(config=config)
    if config is not None:
        config = None if len(config) == 0 else Config(**config)

        

    return config
