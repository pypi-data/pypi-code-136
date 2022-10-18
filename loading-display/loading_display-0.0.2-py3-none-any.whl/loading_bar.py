import time
import math

SPINNER_FRAMES = ["\u25DC ", " \u25DD", " \u25DE", "\u25DF "]
LOADING_UNIT = "\u25AF"


def loading_bar(progress: int,
                max=100,
                length=25,
                show_percentage=False):
    percentage = progress / (max / 100)
    q = math.floor(percentage / (100 / length))
    remaining = length - q
    bar = f'[{LOADING_UNIT * q}{" "*remaining}]'
    if show_percentage:
        print(f'\r{bar} {percentage} %', end='')
    else:
        print(f'\r{bar}', end='')


def spinner():
    current_index = 0
    while 1:
        if current_index >= len(SPINNER_FRAMES) - 1:
            current_index = 0
        else:
            current_index += 1
        yield print(f'\r{SPINNER_FRAMES[current_index]}', end='')


if __name__ == '__main__':
    a = spinner()
    max = 20
    for i in range(0, max):
        next(a)
        time.sleep(0.035)
    print('\r', end='')

    for i in range(0, max+1):
        loading_bar(i, max=max, length=65, show_percentage=True)
        time.sleep(0.035)
    print()
