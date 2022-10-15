import time
import random
from . import config
from .start import main

def make_nightmare():
    message = ""
    for x in range(20):
        message += random.choice(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    gmessage = ""
    for x in message:
        tmessage = random.choice(config.categories["random"][x.lower()])
        if x.isupper():
            tmessage = tmessage.capitalize()
        gmessage += tmessage + " "
    gmessage = gmessage.strip()
    return gmessage

if __name__ == "__main__":
    try:
        main(config)
    except KeyboardInterrupt:
        print("\nHow dare you send a ^C...")
        time.sleep(0.75)
        print(make_nightmare())