from time import sleep


def usleep(microseconds):
    sleep(microseconds / 1.0e6)
