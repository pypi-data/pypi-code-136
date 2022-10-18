from random import randint, random, choice, randrange


def indpredict():
    mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌'
    a = randint(1, 25)
    b = randint(1, 25)
    c = randint(1, 25)
    if a == 1:
        mine1 = "🟩"
    if a == 2:
        mine2 = "🟩"
    if a == 3:
        mine3 = "🟩"
    if a == 4:
        mine4 = "🟩"
    if a == 5:
        mine5 = "🟩"
    if a == 6:
        mine6 = "🟩"
    if a == 7:
        mine7 = "🟩"
    if a == 8:
        mine8 = "🟩"
    if a == 9:
        mine9 = "🟩"
    if a == 10:
        mine10 = "🟩"
    if a == 11:
        mine11 = "🟩"
    if a == 12:
        mine12 = "🟩"
    if a == 13:
        mine13 = "🟩"
    if a == 14:
        mine14 = "🟩"
    if a == 15:
        mine15 = "🟩"
    if a == 16:
        mine16 = "🟩"
    if a == 17:
        mine17 = "🟩"
    if a == 18:
        mine18 = "🟩"
    if a == 19:
        mine19 = "🟩"
    if a == 20:
        mine20 = "🟩"
    if a == 21:
        mine21 = "🟩"
    if a == 12:
        mine22 = "🟩"
    if a == 23:
        mine23 = "🟩"
    if a == 24:
        mine21 = "🟩"
    if a == 25:
        mine25 = "🟩"

    if b == 1:
        mine1 = "🟩"
    if b == 2:
        mine2 = "🟩"
    if b == 3:
        mine3 = "🟩"
    if b == 4:
        mine4 = "🟩"
    if b == 5:
        mine5 = "🟩"
    if b == 6:
        mine6 = "🟩"
    if b == 7:
        mine7 = "🟩"
    if b == 8:
        mine8 = "🟩"
    if b == 9:
        mine9 = "🟩"
    if b == 10:
        mine10 = "🟩"
    if b == 11:
        mine11 = "🟩"
    if b == 12:
        mine12 = "🟩"
    if b == 13:
        mine13 = "🟩"
    if b == 14:
        mine14 = "🟩"
    if b == 15:
        mine15 = "🟩"
    if b == 16:
        mine16 = "🟩"
    if b == 17:
        mine17 = "🟩"
    if b == 18:
        mine18 = "🟩"
    if b == 19:
        mine19 = "🟩"
    if b == 20:
        mine20 = "🟩"
    if b == 21:
        mine21 = "🟩"
    if b == 12:
        mine22 = "🟩"
    if b == 23:
        mine23 = "🟩"
    if b == 24:
        mine21 = "🟩"
    if b == 25:
        mine25 = "🟩"

    if c == 1:
        mine1 = "🟩"
    if c == 2:
        mine2 = "🟩"
    if c == 3:
        mine3 = "🟩"
    if c == 4:
        mine4 = "🟩"
    if c == 5:
        mine5 = "🟩"
    if c == 6:
        mine6 = "🟩"
    if c == 7:
        mine7 = "🟩"
    if c == 8:
        mine8 = "🟩"
    if c == 9:
        mine9 = "🟩"
    if c == 10:
        mine10 = "🟩"
    if c == 11:
        mine11 = "🟩"
    if c == 12:
        mine12 = "🟩"
    if c == 13:
        mine13 = "🟩"
    if c == 14:
        mine14 = "🟩"
    if c == 15:
        mine15 = "🟩"
    if c == 16:
        mine16 = "🟩"
    if c == 17:
        mine17 = "🟩"
    if c == 18:
        mine18 = "🟩"
    if c == 19:
        mine19 = "🟩"
    if c == 20:
        mine20 = "🟩"
    if c == 21:
        mine21 = "🟩"
    if c == 12:
        mine22 = "🟩"
    if c == 23:
        mine23 = "🟩"
    if c == 24:
        mine21 = "🟩"
    if c == 25:
        mine25 = "🟩"

    reter = {"mine1": mine1, "mine2": mine2, "mine3": mine3, "mine4": mine4, "mine5": mine5, "mine6": mine6,
             "mine7": mine7, "mine8": mine8, "mine9": mine9, "mine10": mine10, "mine11": mine11, "mine12": mine12,
             "mine13": mine13, "mine14": mine14, "mine15": mine15, "mine16": mine16, "mine17": mine17,
             "mine18": mine18, "mine19": mine19, "mine20": mine20, "mine21": mine21, "mine22": mine22,
             "mine23": mine23, "mine24": mine24, "mine25": mine25}
    return reter


def intpredict(mine_amount, non, pred):
    if mine_amount == 1:
        empty = []
        for x in range(5):
            grid = [
                f"{non}",
                f"{non}",
                f"{non}",
                f"{non}",
                f"{non}"
            ]
            create_grid = randrange(0, len(grid))
            grid[create_grid] = choice(
                [f"{pred}"])
            empty.append("".join(grid))

    elif mine_amount == 2:
        empty = []
        for x in range(5):
            grid = [
                f"{non}",
                f"{non}",
                f"{non}",
                f"{non}",
                f"{non}"
            ]
            create_grid = randrange(0, len(grid))
            grid[create_grid] = choice([
                f"{pred}"
            ])
            empty.append("".join(grid))

    elif mine_amount == 3:
        empty = []
        for x in range(5):
            grid = [
                f"{non}",
                f"{non}",
                f"{non}",
                f"{non}",
                f"{non}"
            ]
            create_grid = randrange(0, len(grid))
            grid[create_grid] = choice([
                f"{pred}", f"{non}", f"{pred}"
            ])
            empty.append("".join(grid))

    elif mine_amount == 4:
        empty = []
        for x in range(5):
            grid = [
                f"{non}",
                f"{non}",
                f"{non}",
                f"{non}",
                f"{non}"
            ]
            create_grid = randrange(0, len(grid))
            grid[create_grid] = choice([
                f"{pred}", f"{non}",
                f"{non}", f"{pred}"
            ])
            empty.append("".join(grid))

    elif mine_amount == 5:
        empty = []
        for x in range(5):
            grid = [
                f"{non}",
                f"{non}",
                f"{non}",
                f"{non}",
                f"{non}"
            ]
            create_grid = randrange(0, len(grid))
            grid[create_grid] = choice([
                f"{pred}", f"{non}",
                f"{non}"
            ])
            empty.append("".join(grid))
    result = "\n".join(empty)

    return result
