import argparse
import os
import re
import sys


class ArgumentParser(argparse.ArgumentParser):

    def error(self, message):
        message = f"failed to parse command line: {message}"
        raise RuntimeError(message)


def find_available_path(path, ext=None, sep=".", also_match=None):
    original_path = path
    parent_path = os.path.dirname(path)
    number = 1
    ext = ext or ""
    also_match = also_match or []
    if not os.path.isdir(parent_path):
        return f"{path}{ext}"
    while os.path.exists(f"{path}{ext}") or f"{path}{ext}" in also_match:
        number += 1
        path = f"{original_path}{sep}{number}"
    return f"{path}{ext}"


def log(*message, join=" ", end="\n", flush=True):
    message = join.join(str(part) for part in message)
    sys.stderr.write(message)
    sys.stderr.write(end)
    if flush:
        sys.stderr.flush()
    return message


def log_key_value(key, *values, padding=25, end="\n", flush=True):
    key = f"{key}: ".ljust(padding)
    values = ("\n" + " " * padding).join(str(value) or "< blank >" for value in values)
    if not values:
        values = "< blank >"
    return log(key, values, join="", end=end, flush=flush)


def abort():
    sys.stderr.write("aborted\n")
    raise SystemExit(0)


def ask_continue(prompt="continue?", default=None):
    response = None
    while response not in ["y", "yes", "n", "no"]:
        if response is not None:
            sys.stderr.write("\r")
        sys.stderr.write(f"{prompt} [y/n] ")
        if os.isatty(sys.stdin.fileno()):
            response = input()
        else:
            if default is None:
                raise RuntimeError("unable to get answer and no default")
            response = "y" if default else "n"
            sys.stderr.write(f"{response}\n")
    return response in ["y", "yes"]


def validate_setting(key, value, validation):
    def warning(info=None):
        return \
            f"setting {key} failed validation:\n" \
            f"    required: {' '.join(validation)}\n" \
            f"    specified: {value or '< blank >'}{f' ({info})' if info else ''}"
    if validation[0] == "optional":
        if value is None or value == "":
            return "", None
        validation = validation[1:]
    if value is None:
        raise ValueError(f"setting {key} not specified")
    if validation[0] in ["", "any"]:
        pass
    elif validation[0] == "path":
        expanded = os.path.expandvars(value)
        if len(validation) == 1:
            pass
        elif validation[1] == "exists":
            if not os.path.exists(expanded):
                return value, warning()
        elif validation[1] == "file_exists":
            if not os.path.isfile(expanded):
                return value, warning()
        elif validation[1] == "dir_exists":
            if not os.path.isdir(expanded):
                return value, warning()
        elif validation[1] == "base_exists":
            parent = os.path.dirname(expanded)
            if os.path.isdir(parent):
                base_name = os.path.basename(expanded)
                for file in os.listdir(parent):
                    if file.startswith(base_name):
                        break
                else:
                    return value, warning()
            else:
                return value, warning()
        else:
            raise ValueError(f"invalid path validation: {validation}")
    elif validation[0] == "number":
        if re.match(r"^[+-]?([0-9]*[.])?[0-9]+$", value):
            if len(validation) > 1:
                if not eval(value + " " + " ".join(validation[1:])):
                    return value, warning()
        else:
            return value, warning()
    elif validation[0] == "integer":
        if re.match(r"^[+-]?[0-9]+$", value):
            if len(validation) > 1:
                if not eval(value + " " + " ".join(validation[1:])):
                    return value, warning()
        else:
            return value, warning()
    elif validation[0] == "regex":
        if not re.match(rf"^{validation[1]}$", value):
            return value, warning()
    elif validation[0] == "choice":
        choices = validation[1].split("|")
        if value not in choices:
            return value, warning()
    elif validation[0] == "duration":
        validation[0] = "duration as hh:mm:ss"
        if not re.match(r"\d\d:\d\d:\d\d", value):
            return value, warning()
        if int(value[3:5]) >= 60 or int(value[6:8]) >= 60:
            return value, warning()
        if "".join(validation[1:3]) == ">0" and not int(value.replace(":", "")):
            return value, warning()
    else:
        raise ValueError(f"invalid setting validation: {validation}")
    return value, None
