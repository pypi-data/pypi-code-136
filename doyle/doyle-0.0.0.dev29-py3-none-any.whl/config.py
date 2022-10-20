import os
import pathlib

__root__  = pathlib.PurePath(os.path.dirname(os.path.abspath(__file__))).as_posix()
__statics__ = f"{__root__}/statics"
