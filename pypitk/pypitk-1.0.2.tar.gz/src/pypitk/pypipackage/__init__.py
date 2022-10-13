from dataclasses import dataclass,field
from .util import get_package_dir as _get_package_dir
from .paths import Paths
from .config import Config, init_config as _init_config
from .content import Content

@dataclass(frozen=False,order=True)
class PYPIPackage:

    config:Config = field(init=True)
    def __init__(self, __config: Config = None):
        self.config = _init_config() if __config is None else __config

    @property
    def package_dir(self):
        return _get_package_dir(self.config)

    @property
    def package_name(self):
        return self.config["package_name"]

    @property
    def subdir_structure(self):
        return [
            "pyproject.toml",
            "MANIFEST.in",
            "README.md",
            "private.txt",
            {"tests": ["__init__.py", f"test_{self.package_name}.py"]},
            {"src": ["__init__.py", {self.package_name: ["__init__.py"]}]},
        ]

    @property
    def paths(self):
        return Paths(self.package_dir)

    @property
    def content(self):
        return Content(self.config)
