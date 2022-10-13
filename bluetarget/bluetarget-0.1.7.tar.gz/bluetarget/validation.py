from typing import List

import os
import pathlib

from bluetarget.errors import FileNotFound, ModelClassNotFound


def validate_files(files: List[str]) -> None:
    for file in files:
        if os.path.exists(file) == False:
            raise FileNotFound(file)


def validate_model_class(model_class: str, files: List[str]) -> str:
    files = list(filter(lambda f: pathlib.Path(f).suffix == ".py", files))

    for file in files:
        text_file = open(file, "r")
        raw_data = text_file.read()
        text_file.close()

        if raw_data.find(model_class) != -1:
            return file

    raise ModelClassNotFound(model_class)
