ICONSOLE = True

"""PYPIPR Module"""
try:
    ICONSTANT
except:
    from .iconstant import *


"""PYTHON Standard Module"""
import subprocess


"""PYPI Module"""
import colorama

if WINDOWS:
    import msvcrt as _getch
else:
    import getch as _getch


colorama.init()


def print_colorize(
    text,
    color=colorama.Fore.GREEN,
    bright=colorama.Style.BRIGHT,
    color_end=colorama.Style.RESET_ALL,
    text_start="\n",
    text_end="\n",
):
    """Print text dengan warna untuk menunjukan text penting"""
    print(f"{text_start}{color + bright}{text}{color_end}", end=text_end, flush=True)


def log(text):
    """
    Melakukan print ke console untuk menginformasikan proses yg sedang berjalan didalam program.
    """

    def inner_log(func):
        print_colorize(f">>> {text}", text_end="")

        def callable_func(*args, **kwargs):
            result = func(*args, **kwargs)
            return result

        return callable_func

    return inner_log


def run(command):
    """Menjalankan command seperti menjalankan command di Command Terminal"""
    return subprocess.run(command, shell=True)


def input_char(prompt=None, prompt_ending="", newline_after_input=True):
    """Meminta masukan satu huruf tanpa menekan Enter. Masukan tidak ditampilkan."""
    if prompt:
        print(prompt, end=prompt_ending, flush=True)
    g = _getch.getch()
    if newline_after_input:
        print()
    return g


def input_char_echo(prompt=None, prompt_ending="", newline_after_input=True):
    """Meminta masukan satu huruf tanpa menekan Enter. Masukan akan ditampilkan."""
    if prompt:
        print(prompt, end=prompt_ending, flush=True)
    g = _getch.getche()
    if newline_after_input:
        print()
    return g
