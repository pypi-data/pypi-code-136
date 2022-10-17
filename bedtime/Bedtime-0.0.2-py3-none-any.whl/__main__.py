import time

import __init__ as bedtime

def stamp():
    return time.strftime('[%H:%M:%S]', time.localtime())

def log_info(msg):
    with open("./test.log", "a") as f:
        f.write(msg + "\n")


def log_sleep():
    log_info(F"{stamp()} slept")

def log_shutdown():
    log_info(F"{stamp()} slept very nicely")

sleeper = bedtime.Listener(on_sleep=log_sleep, on_shutdown=log_shutdown)

while True:
    time.sleep(1)