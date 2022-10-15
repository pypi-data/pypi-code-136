import os
import time
import random
from datetime import datetime
from . import __full_title__ as name

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

    print(f"Welcome to '{name}'!")
    time.sleep(1)

    print("")
    author = input("Message Author: ").strip()
    time.sleep(0.25)

    message = input("Message: ").strip()
    time.sleep(0.25)

    _types = []
    for category in config.categories:
        _types.append(category)
    types = ", ".join(_types)
    while True:
        type = input(f"Choose quote category:\n{types}\n> ").strip().lower()
        if type in _types:
            break
        else:
            print("Invalid category!\n")
            time.sleep(0.25)
    print(f"\n\nAuthor: {author}\nMessage: {message}\nCategory: {type}")

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
        print(gmessage)
        return "\nGenerated quote:\n" + make_message(gmessage, author, date())

    print(make_quote())
    time.sleep(0.25)

    while True:
        inp = input("Do you want to generate quote again? (Y/n) ").strip().lower()
        if inp == "" or inp == "y" or inp == "yes":
            print(make_quote())
        elif inp == "n" or inp == "no":
            exit()
        else:
            print("Invalid Input!")
            exit()