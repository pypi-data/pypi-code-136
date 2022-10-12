from pathlib import Path

from .dotdict import DotDict
from .json_mixin import JSONLoaderMixin


class Input(DotDict, JSONLoaderMixin):
    def __init__(
        self,
        input_fp: str | Path | None = None,
        input_dict: dict | None = None,
        jsonpaths: bool = False,
    ):
        if input_fp is not None:
            self.fp = input_fp
            self.load()  # ensures existence of self.json attribute
        elif input_dict is not None:
            self.load_dict(input_dict)  # ensures existence of self.json attribute
        else:
            raise ValueError("Need input filepath or input dictionary.")

        super().__init__(self.json, name="Input", jsonpaths=jsonpaths)
        return
