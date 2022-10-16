import random


def trollify(inputString: str):
    copy = inputString
    for i in copy:
        chance = random.randint(0, 9)
        if i <= 4:
            copy[i].capitalize()
        else:
            pass
    return copy
