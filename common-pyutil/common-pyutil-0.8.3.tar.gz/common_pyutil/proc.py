from typing import List, Union, Optional, Tuple
import platform
from subprocess import Popen, PIPE


def call(cmd: Union[str, List[str]], input: str = "",
         timeout: Optional[Union[int, float]] = None) -> Tuple[str, str]:
    """Call a process with command :code:`cmd` caputre outputs and return.

    Args:
        cmd: The command line for the process to open
        timeout: Timeout for the command

    """
    if timeout:
        if input:
            p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            out, err = p.communicate(input=input.encode(),
                                     timeout=timeout)
        else:
            p = Popen(cmd, stdout=PIPE, stderr=PIPE)
            out, err = p.communicate(timeout=timeout)
    else:
        if input:
            p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            out, err = p.communicate(input=input.encode())
        else:
            p = Popen(cmd, stdout=PIPE, stderr=PIPE)
            out, err = p.communicate()
    return out.decode("utf-8").strip(), err.decode("utf-8").strip()


def which(cmd: str):
    """Return the full path of a program if it exists on system.

    System can be a windows or unix like sytem

    Args:
        cmd: Name of the program

    """
    sys_name = platform.system().lower()
    if sys_name == "linux":
        cmd = "which"
    elif sys_name == "windows":
        cmd = "where"
    else:
        raise ValueError(f"Unknown system {sys_name}")
    return call(cmd)[0]
