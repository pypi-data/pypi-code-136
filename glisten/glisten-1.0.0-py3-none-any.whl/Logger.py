import math
import re

import colorama
from colorama import Fore, Style, Back
from tqdm import tqdm

class Logger():
    def __init__(self, log_file_location: str='.log',
                       verbose_mode: bool=True,
                       line_length_break: int=72):

        self._logfile = log_file_location
        self._verbose = verbose_mode
        self._write_to_disk = False
        self._auto_line_length_break = line_length_break

    def get_max_line_length(self):
        return self._auto_line_length_break

    def __enter__(self):
        colorama.init()
        self._logfile_pointer = open(self._logfile, 'w')
        self._write_to_disk = True
        return self

    def _log_to_disk(self, type, message):
        if self._write_to_disk:
            message = message.replace("\n", " ")
            self._logfile_pointer.writelines(f"[{type}] {message}\n")

    def _decorate(self, header: str, color, modifier, message: str, sep_char: str="|"):
        header = header[0].upper() + header[1:].lower()

        line_length_break = self._auto_line_length_break

        if len(message) > line_length_break and "\n" not in message:
            # Break it up ourselves.
            i = 0
            offset = 1
            while i <= len(message):
                part = message[i:i+line_length_break]
                idx = part.rfind(" ")
                message = message[:i+idx+offset] + "\n" + message[i+idx+offset:]

                i += line_length_break

            message = message.replace("\n\n", "\n")

        spacer = " " * (len(header) + 3)
        half_space = " " * math.floor(((len(header) + 3)/2))

        if (len(header) + 3) % 2: #odd length
            first_space = half_space
            second_space = half_space
        else:
            first_space = half_space[:-1]
            second_space = half_space

        message = message.replace("\n", f"\n{first_space}{sep_char}{second_space}")

        return f"{color}{modifier}[{header}]{Style.RESET_ALL} {message}"

    def types(self):
        types = dir(self)
        retobj = []

        for T in types:
            if T not in ['deprecate', 'types']:
                if T[0] != "_":
                    retobj.append(T)

        return retobj

    def _print(self, message):
        tqdm.write(message)

    def info(self, message):
        decorated_message = self._decorate("info",
                                           Fore.CYAN,
                                           Style.DIM,
                                           message)

        if self._verbose:
            self._print(decorated_message)

        self._log_to_disk("info", message)

    def status(self, message):
        decorated_message = self._decorate("status",
                                           Fore.GREEN,
                                           Style.BRIGHT,
                                           message)

        if self._verbose:
            self._print(decorated_message)

        self._log_to_disk("info", message)

    def warn(self, message):
        decorated_message = self._decorate("warning",
                                           Fore.YELLOW,
                                           Style.DIM,
                                           message)

        if self._verbose:
            self._print(decorated_message)

        self._log_to_disk("warning", message)

    def error(self, message):
        decorated_message = self._decorate("Error",
                                           Fore.WHITE,
                                           Back.RED,
                                           message)

        if self._verbose:
            self._print(decorated_message)

        self._log_to_disk("error", message)

    def deprecated(self, message):
        decorated_message = self._decorate("deprecation",
                                           Fore.BLUE,
                                           Style.DIM,
                                           message)

        if self._verbose:
            self._print(decorated_message)

        self._log_to_disk("deprecated", message)

    def deprecate(self, func, warning='default'):
        if warning == 'default':
            warning = f"Function \"{func.__name__}\" is deprecated."
        def wrapper(*args, **kwargs):
            self.deprecated(warning)
            func(*args, **kwargs)
        return wrapper


    def __exit__(self, exc_type, exc_value, traceback):
        self._write_to_disk = False
        self._logfile_pointer.close()
