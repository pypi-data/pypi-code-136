from typing import List

import os
import shutil
import zipfile
from pathlib import Path

from bluetarget.constants import CODE_DIR


def clean_tmp():
    shutil.rmtree(CODE_DIR)


def prepare_package(files: List[str]) -> str:

    if Path.exists(CODE_DIR) == False:
        os.mkdir(CODE_DIR)

    package = f'{CODE_DIR}/package.zip'

    with zipfile.ZipFile(package, mode="w") as archive:
        for file in files:
            archive.write(file)

    return package
