from .. import config

import os
import glob
import gdown
import sys
import subprocess

def exists_sherlock_necessary():
    return os.path.exists(f"{config.__statics__}/sherlock_files") \
        and os.path.exists(f"{config.__statics__}/model_files") \
            and os.path.exists(f"{config.__statics__}/feature_column_identifiers")

def initial_sherlock_necessary():
    if not exists_sherlock_necessary():
        output = f"{config.__statics__}/sherlock_necessary.zip"
        tmp_files = glob.glob(f"{output}*tmp")

        gdown.download(
            url="https://drive.google.com/file/d/1Ywoj5wakWvtaid3oEdV1YT-cc2yF0HzT/view?usp=sharing",
            output=output,
            quiet=False, 
            fuzzy=True,
            resume=(len(tmp_files) > 0),
        )

        gdown.extractall(output)
        files = glob.glob(f"{output}*")
        for f in files:
            try: os.remove(f)
            except PermissionError as e:
                print(e)

def sherlock_installing():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", 
        "git+https://github.com/mitmedialab/sherlock-project.git#egg=sherlock"])