import os
import time
import atexit
import random
import readline
from datetime import datetime
from . import (
    __full_title__ as name,
    __version__ as version,
    __copyright__ as copyright,
    __title__ as title,
    color
)

__all__ = [
    "main"
]

def main(config) -> None:
    """
    Start the program

    Args:
        config: config class
    """
    if not config.history_file_name in os.listdir(config.history_file_dir):
        open(config.history_file_path, "w").close()
    atexit.register(readline.write_history_file, config.history_file_path)
    
    make_message = lambda quote, author, date: config.message.format(
        quote = quote,
        author = author,
        date = date
    )
    def date():
        return datetime.now().strftime(config.date_format)

    print(f"{color.bright_green}{name} {color.bright_white}| {color.reset}{color.bright_magenta}{copyright}\n{color.bright_blue}{color.underline}{title}{color.reset} {color.bright_yellow}v{color.bright_cyan}{version}{color.reset}")
    print(f"\n{color.red}{color.underline}Be scared{color.reset}{color.red}. {color.bright_red}You know why.{color.reset}")
    time.sleep(1)

    print()
    author = input(f"{color.bright_blue}Message Author{color.reset}:\n> {color.bright_white}").strip()
    if author == "":
        author = "unknown"
    time.sleep(0.25)

    message = input(f"\n{color.bright_blue}Message{color.reset}:\n> {color.bright_white}").strip()
    time.sleep(0.25)

    _types = []
    for category in config.categories:
        _types.append(category)
    types = f"{color.reset}, {color.bright_yellow}".join(_types)
    while True:
        type = input(f"\n{color.bright_blue}Choose quote category{color.reset}:\n{color.bright_yellow}{types}\n{color.reset}> {color.bright_white}").strip().lower()
        if type in _types:
            break
        else:
            print(f"{color.red}Invalid category!{color.reset}\n")
            time.sleep(0.25)
    print(f"\n\n{color.bright_blue}Author{color.reset}: {color.bright_white}{author}\n{color.bright_blue}Message{color.reset}: {color.bright_white}{message}\n{color.bright_blue}Category{color.reset}: {color.bright_white}{type}{color.reset}")

    def make_quote():
        gmessage = ""
        for x in message:
            if x.lower() not in config.categories[type]:
                gmessage += x
                continue
            tmessage = random.choice(config.categories[type][x.lower()])
            if x.isupper():
                tmessage = tmessage.capitalize()
            gmessage += tmessage + " "
        gmessage = gmessage.strip()
        return f"\n{color.bright_green}Generated quote{color.reset}:\n{color.blue}{color.reversed}" + make_message(gmessage, author, date()) + color.reset

    print(make_quote())
    time.sleep(0.25)

    while True:
        inp = input(f"\n{color.bright_yellow}Do you want to generate quote again? {color.reset}({color.bright_green}Y{color.reset}/{color.bright_red}n{color.reset}) {color.bright_white}").strip().lower()
        if inp == "" or inp == "y" or inp == "yes":
            print(make_quote())
        elif inp == "n" or inp == "no":
            print(color.reset, end="")
            exit()
        else:
            print(f"{color.red}Invalid input!{color.reset}")
            exit()