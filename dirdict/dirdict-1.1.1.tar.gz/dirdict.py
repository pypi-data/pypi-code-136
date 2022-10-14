from pathlib import Path
from typing import Any, Union, Iterator


class DirDict:
    path: Path

    def __init__(self, path: str | Path = Path(".")):
        self.path = path if isinstance(path, Path) else Path(path)
        if not self.path.exists():
            self.path.mkdir()
        if not self.path.is_dir():
            raise EnvironmentError("DirDict path must be a directory or non-existing")

    def __setitem__(self, name: str | Path, item: bytes):
        with open(self.path / name, "wb") as f:
            f.write(item)

    def __getitem__(self, name: str | Path) -> Union[bytes, "DirDict"]:
        filepath = self.path / name
        if filepath.is_dir():
            return DirDict(filepath)
        with open(filepath, "rb") as f:
            return f.read()

    def get(self, key: str | Path, default: Any = None) -> Any:
        if key in self:
            return self[key]
        else:
            return default

    def __contains__(self, key: str | Path) -> bool:
        if isinstance(key, Path):
            return key.resolve().exists()
        else:
            return key in self.keys()

    def __truediv__(self, other: str | Path) -> "DirDict":
        return DirDict(path=self.path / other)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, DirDict):
            return other.path.resolve() == self.path.resolve()
        return False

    def __delitem__(self, name: str | Path) -> None:
        targetpath = self.path / name
        if targetpath.is_dir():
            targetpath.rmdir()
        else:
            targetpath.unlink()

    def __iter__(self) -> Iterator[str]:
        return self.keys()

    def keys(self) -> Iterator[str]:
        return (p.name for p in self.path.glob("*"))

    def values(self) -> Iterator[Union[bytes, "DirDict"]]:
        return (self[p.name] for p in self.path.glob("*"))

    def items(self) -> Iterator[tuple[str, Union[bytes, "DirDict"]]]:
        return ((p.name, self[p.name]) for p in self.path.glob("*"))

    def __hash__(self) -> int:
        return hash(self.path.resolve())
