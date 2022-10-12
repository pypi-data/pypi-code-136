import subprocess
from typing import List

from pydmt.configs import ConfigSubprocess


def check_call(args: List[str]):
    if ConfigSubprocess.print_command:
        print(f"running {args}")
    if ConfigSubprocess.quiet:
        subprocess.check_call(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        subprocess.check_call(args)
