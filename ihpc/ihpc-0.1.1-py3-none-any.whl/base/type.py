__all__ = ['AnyPosixPath', 'Path', 'StdIOE', 'StdOE', 'Table']


import pathlib as p
import typing as t

if t.TYPE_CHECKING:
    from .core import RemotePath


AnyPosixPath = t.Union[p.Path, 'RemotePath']
Path = t.Union[str, p.Path]
StdIOE = t.Tuple[bytes, bytes, bytes]
StdOE = t.Tuple[bytes, bytes]


class Table:
    def __class_getitem__(cls, T: type) -> type:
        return t.List[t.Dict[str, T]]
