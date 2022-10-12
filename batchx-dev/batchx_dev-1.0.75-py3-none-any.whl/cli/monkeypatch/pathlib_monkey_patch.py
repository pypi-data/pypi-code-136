from pathlib import Path

# monkey patch
def _remove(self):
    from shutil import rmtree

    if self.is_file():
        self.unlink()
    else:
        rmtree(self.absolute())
    return


def _copy(self, target):
    from shutil import copy

    target = Path(target)

    assert self.is_file(), "Copy only defined on files!"

    if target.is_dir():
        target_fp = target / self.name
    else:
        target_fp = target

    copy(str(self), str(target_fp))
    return target_fp


Path.copy = _copy
Path.cp = _copy
Path.remove = _remove
Path.rm = _remove
