import osiotk as _os


class Paths:
    def __init__(self, package_dir: str):
        self.package_dir = package_dir

    @property
    def pyproject_toml(self) -> str:
        return _os.join_paths(self.package_dir, "pyproject.toml")

    @property
    def readme(self) -> str:
        return _os.join_paths(self.package_dir, "README.md")

    @property
    def private(self) -> str:
        return _os.join_paths(self.package_dir, "private.txt")
