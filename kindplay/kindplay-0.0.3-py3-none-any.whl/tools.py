import shlex
import os

from subprocess import Popen, PIPE


def run_command(command, stdout=PIPE, stderr=PIPE, cwd=None, env=None):
    """Run command line and return ."""
    command = shlex.split(command)
    cmd_output = ""
    cmd_error = ""
    try:
        cmd = Popen(command, stderr=stderr, stdout=stdout, cwd=cwd, env=env)
        stdout, stderr = cmd.communicate()
        return_code = cmd.returncode
        if stdout:
            cmd_output = stdout.decode()
        if stderr:
            cmd_error = stderr.decode()
    except FileNotFoundError:
        return_code = 1
        cmd_error = f"Command {command[0]} not found"
        if stderr != PIPE:
            print(cmd_error, flush=True)
    except:
        raise

    return {"return_code": return_code, "output": cmd_output, "error": cmd_error}