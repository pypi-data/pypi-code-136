import random
from random import randint as rand
import time


def random_string(length=None, verbose=False, alpha=False, alpha_numeric=False):
    t1 = int(time.time() * 1000)

    if not length:
        length = random.randint(1, 100)
        if verbose:
            print(f'Length not provided, generating random length string ({length})')

    string = ''

    for x in range(length):
        char_list = [chr(rand(97, 97 + 25)), chr(rand(65, 65 + 25)), chr(rand(48, 48 + 9)), chr(rand(33, 127))]
        string += char_list[rand(0, 1 if alpha else 2 if alpha_numeric else 3)]

    t2 = int(time.time() * 1000)

    if verbose:
        print(f'string generated in {t2 - t1} ms')

    return string
