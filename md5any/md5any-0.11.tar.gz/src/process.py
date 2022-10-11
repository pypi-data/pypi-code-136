from pathlib import Path

from .error import MD5AnyErrorCode
from .hash import hash

class Hash:
    def __init__(self, path):
        self._abs = self._hash_dir(path) if Path(path).is_dir() else self._hash_file(path)

    @property
    def absrtact(self):
        return self._abs

    @staticmethod
    def test(path):
        if not Path(path).exists():
            errorMsg = "Invalid path {}".format(path)
            raise MD5AnyErrorCode(errorMsg)
        return path

    def _hash_file(self, filepath, dentry=None):
        if Path(filepath).is_dir():
            raise MD5AnyErrorCode("Not a regular file")

        try:
            with Path(filepath).open('rb') as f:
                abs = hash(str(f.read()))
                if dentry is not None:
                    abs = hash(str(dentry) + str(abs))
                return abs
        except:
            raise MD5AnyErrorCode("Hash failed")

    def _hash_dir(self, dirpath, dentry='.'):
        if not Path(dirpath).is_dir():
            raise MD5AnyErrorCode("Not a regular directory")

        hashList = []
        path = Path(dirpath)
        for item in path.iterdir():
            if item.is_dir():
                hashList.append(self._hash_dir(str(item), str(item.name)))
            if item.is_file():
                hashList.append(self._hash_file(str(item), Path(dentry).joinpath(str(item.name))))
        hashList.sort()
        abs = hash(str(dentry) + ''.join(hashList))
        return abs
