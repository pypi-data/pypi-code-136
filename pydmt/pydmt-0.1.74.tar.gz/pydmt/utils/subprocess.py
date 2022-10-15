import os
import subprocess
from typing import List

from pydmt.configs import ConfigSubprocess


def check_call(args: List[str]) -> None:
    if ConfigSubprocess.print_command:
        print(f"running {args}")
    if ConfigSubprocess.quiet:
        subprocess.check_call(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        subprocess.check_call(args)


def check_call_ve(args: List[str]) -> None:
    virtual_env = os.getenv("VIRTUAL_ENV")
    assert virtual_env is not None, "not in virtual env"
    args[0] = os.path.join(virtual_env, "bin", args[0])
    if ConfigSubprocess.print_command:
        print(f"running {args}")
    if ConfigSubprocess.quiet:
        subprocess.check_call(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        subprocess.check_call(args)
