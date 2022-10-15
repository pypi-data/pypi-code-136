import os
import time
import random
from datetime import datetime
from . import (
    __full_title__ as name,
    __version__ as version,
    __copyright__ as copyright,
    __title__ as title
)

class color:
    black = "\u001b[30m"
    red = "\u001b[31m"
    green = "\u001b[32m"
    yellow = "\u001b[33m"
    blue = "\u001b[34m"
    magenta = "\u001b[35m"
    cyan = "\u001b[36m"
    white = "\u001b[37m"
    bright_black = "\u001b[30;1m"
    bright_red = "\u001b[31;1m"
    bright_green = "\u001b[32;1m"
    bright_yellow = "\u001b[33;1m"
    bright_blue = "\u001b[34;1m"
    bright_magenta = "\u001b[35;1m"
    bright_cyan = "\u001b[36;1m"
    bright_white = "\u001b[37;1m"
    bold = "\u001b[1m"
    underline = "\u001b[4m"
    reversed = "\u001b[7m"
    reset = "\u001b[0m"

def main(config) -> None:
    """
    Start the program

    Args:
        config: config class
    """
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

    print("")
    author = input(f"{color.bright_blue}Message Author{color.reset}: {color.bright_white}").strip()
    time.sleep(0.25)

    message = input(f"{color.bright_blue}Message{color.reset}: {color.bright_white}").strip()
    time.sleep(0.25)

    _types = []
    for category in config.categories:
        _types.append(category)
    types = f"{color.reset}, {color.bright_yellow}".join(_types)
    while True:
        type = input(f"{color.bright_blue}Choose quote category{color.reset}:\n{color.bright_yellow}{types}\n{color.reset}> {color.bright_white}").strip().lower()
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
        return f"\n{color.bright_green}Generated quote{color.reset}:\n{color.blue}" + make_message(gmessage, author, date()) + color.reset

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