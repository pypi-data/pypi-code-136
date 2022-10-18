from subprocess import run as _run


def run(command: str, check=True):
    result = _run(command, check=check, shell=True)
    return {
        "exit_code": result.returncode
    }
