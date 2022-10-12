from random import randint


def roll(number_dice: int, number_face: int):

    try:

        if (int(number_dice)) > 1 and (int(number_face)) >= 2:
            for dice in range(int(number_dice)):
                print(f"{dice}º dice: {randint(1, int(number_face))}\n")
        else:
            print("invalid command")
    except:
        print("invalid command")
