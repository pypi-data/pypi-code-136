from functools import reduce
import math
from .constants import *


def get_pg01() -> dict:
    """
    Problem G01
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return 5 * sum([x[i] for i in range(4)]) - 5 * sum([x[i] for i in range(4)]) - \
               sum([x[i] for i in range(4, 13)])

    def g1(*x):
        return 2 * x[0] + 2 * x[1] + x[9] + x[10] - 10

    def g2(*x):
        return 2 * x[0] + 2 * x[2] + x[9] + x[11] - 10

    def g3(*x):
        return 2 * x[1] + 2 * x[2] + x[10] + x[11] - 10

    def g4(*x):
        return - 8 * x[0] + x[9]

    def g5(*x):
        return - 8 * x[1] + x[10]

    def g6(*x):
        return - 8 * x[2] + x[11]

    def g7(*x):
        return - 2 * x[3] - x[4] + x[9]

    def g8(*x):
        return - 2 * x[5] - x[6] + x[10]

    def g9(*x):
        return - 2 * x[7] - x[8] + x[11]

    ranges = [*[[0, 1] for _ in range(9)], *[[0, 100] for _ in range(9, 12)], [0, 1]]

    x_best = [1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 1]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g1, g2, g3, g4, g5, g6, g7, g8, g9],
        "hx": [],
        "ranges": ranges,
        "markdown": PROBLEM_G01,
        "x": x_best,
        "fx": fx_best
    }


def get_pg02(n: int = 20) -> dict:
    """
    Problem G02
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        f1 = sum([math.cos(xi) ** 4 for xi in x])
        f2 = 2 * reduce(lambda a, b: a * b, [math.cos(xi) ** 2 for xi in x])
        f3 = math.sqrt(sum([(i + 1) * (x[i] ** 2) for i in range(len(x))]))
        return - abs((f1 - f2) / f3)

    def g1(*x):
        return 0.75 - reduce(lambda a, b: a * b, x)

    def g2(*x):
        return sum(x) - 7.5 * n

    ranges = [[10**-4, 10] for _ in range(n)]

    x_best = [3.16246061572185, 3.12833142812967, 3.09479212988791, 3.06145059523469, 3.02792915885555,
              2.99382606701730, 2.95866871765285, 2.92184227312450, 0.49482511456933, 0.48835711005490,
              0.48231642711865, 0.47664475092742, 0.47129550835493, 0.46623099264167, 0.46142004984199,
              0.45683664767217, 0.45245876903267, 0.44826762241853, 0.44424700958760, 0.44038285956317]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g1, g2],
        "hx": [],
        "ranges": ranges,
        "markdown": PROBLEM_G02,
        "x": x_best,
        "fx": fx_best
    }


def get_pg03(n: int = 10) -> dict:
    """
    Problem G03
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return - (math.sqrt(n) ** n) * reduce(lambda a, b: a * b, x)

    def h1(*x):
        return sum([xi ** 2 for xi in x]) - 1

    ranges = [[0, 1] for _ in range(n)]

    if n == 10:
        x_best = [0.31624357647283069, 0.316243577414338339, 0.316243578012345927, 0.316243575664017895,
                  0.316243578205526066, 0.31624357738855069, 0.316243575472949512, 0.316243577164883938,
                  0.316243578155920302, 0.316243576147374916]

        fx_best = objective_function(*x_best)
    else:
        x_best = None
        fx_best = None

    return {
        "objective_function": objective_function,
        "gx": [],
        "hx": [h1],
        "ranges": ranges,
        "markdown": PROBLEM_G03,
        "x": x_best,
        "fx": fx_best
    }


def get_pg04() -> dict:
    """
    Problem G04
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return 5.3578547 * x[2] ** 2 + 0.8356891 * x[0] * x[4] + 37.293239 * x[0] - 40792.141

    def g1(*x):
        return 85.334407 + 0.0056858 * x[1] * x[4] + 0.0006262 * x[0] * x[3] - 0.0022053 * x[2] * x[4] - 92

    def g2(*x):
        return - 85.334407 - 0.0056858 * x[1] * x[4] - 0.0006262 * x[0] * x[3] + 0.0022053 * x[2] * x[4]

    def g3(*x):
        return 80.51249 + 0.0071317 * x[1] * x[4] + 0.0029955 * x[0] * x[1] + 0.0021813 * x[2] ** 2 - 110

    def g4(*x):
        return - 80.51249 - 0.0071317 * x[1] * x[4] - 0.0029955 * x[0] * x[1] - 0.0021813 * x[2] ** 2 + 90

    def g5(*x):
        return 9.300961 + 0.0047026 * x[2] * x[4] + 0.0012547 * x[0] * x[2] + 0.0019085 * x[2] * x[3] - 25

    def g6(*x):
        return - 9.300961 - 0.0047026 * x[2] * x[4] - 0.0012547 * x[0] * x[2] - 0.0019085 * x[2] * x[3] + 20

    ranges = [[78, 102], [33, 45], *[[27, 45] for _ in range(3)]]

    x_best = [78, 33, 29.9952560256815985, 45, 36.7758129057882073]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g1, g2, g3, g4, g5, g6],
        "hx": [],
        "ranges": ranges,
        "markdown": PROBLEM_G04,
        "x": x_best,
        "fx": fx_best
    }


def get_pg05() -> dict:
    """
    Problem G05
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return 3.0 * x[0] + 0.000001 * x[0] ** 3 + 2 * x[1] + (0.000002 / 3.0) * x[1] ** 3

    def g1(*x):
        return - x[3] + x[2] - 0.55

    def g2(*x):
        return - x[2] + x[3] - 0.55

    def h1(*x):
        return 1000 * math.sin(- x[2] - 0.25) + 1000 * math.sin(- x[3] - 0.25) + 894.8 - x[0]

    def h2(*x):
        return 1000 * math.sin(x[2] - 0.25) + 1000 * math.sin(x[2] - x[3] - 0.25) + 894.8 - x[0]

    def h3(*x):
        return 1000 * math.sin(x[3] - 0.25) + 1000 * math.sin(x[3] - x[2] - 0.25) + 1924.8

    ranges = [[0, 1200], [0, 1200], [-0.55, 0.55], [-0.55, 0.55]]

    x_best = [679.945148297028709, 1026.06697600004691, 0.118876369094410433, -0.39623348521517826]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g1, g2],
        "hx": [h1, h2, h3],
        "ranges": ranges,
        "markdown": PROBLEM_G05,
        "x": x_best,
        "fx": fx_best
    }


def get_pg06() -> dict:
    """
    Problem G06
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return (x[0] - 10.0) ** 3 + (x[1] - 20.0) ** 3

    def g1(*x):
        return -(x[0] - 5) ** 2 - (x[1] - 5) ** 2 + 100

    def g2(*x):
        return (x[0] - 6) ** 2 + (x[1] - 5) ** 2 - 82.81

    ranges = [[13, 100], [0, 100]]

    x_best = [14.09500000000000064, 0.8429607892154795668]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g1, g2],
        "hx": [],
        "ranges": ranges,
        "markdown": PROBLEM_G06,
        "x": x_best,
        "fx": fx_best
    }


def get_pg07() -> dict:
    """
    Problem G07
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return (x[0] ** 2 + x[1] ** 2 + x[0] * x[1] - 14 * x[0] - 16 * x[1] + (x[2] - 10) ** 2 +
                4 * (x[3] - 5) ** 2 + (x[4] - 3) ** 2 + 2 * (x[5] - 1) ** 2 + 5 * x[6] ** 2 +
                7 * (x[7] - 11) ** 2 + 2 * (x[8] - 10) ** 2 + (x[9] - 7) ** 2 + 45)

    def g1(*x):
        return -105 + 4 * x[0] + 5 * x[1] - 3 * x[6] + 9 * x[7]

    def g2(*x):
        return 10 * x[0] - 8 * x[1] - 17 * x[6] + 2 * x[7]

    def g3(*x):
        return - 8 * x[0] + 2 * x[1] + 5 * x[8] - 2 * x[9] - 12

    def g4(*x):
        return 3 * (x[0] - 2) ** 2 + 4 * (x[1] - 3) ** 2 + 2 * x[2] ** 2 - 7 * x[3] - 120

    def g5(*x):
        return 5 * x[0] ** 2 + 8 * x[1] + (x[2] - 6) ** 2 - 2 * x[3] - 40

    def g6(*x):
        return x[0] ** 2 + 2 * (x[1] - 2) ** 2 - 2 * x[0] * x[1] + 14 * x[4] - 6 * x[5]

    def g7(*x):
        return 0.5 * (x[0] - 8) ** 2 + 2 * (x[1] - 4) ** 2 + 3 * x[4] ** 2 - x[5] - 30

    def g8(*x):
        return - 3 * x[0] + 6 * x[1] + 12 * (x[8] - 8) ** 2 - 7 * x[9]

    ranges = [[-10, 10] for _ in range(10)]

    x_best = [2.17199634142692, 2.3636830416034, 8.77392573913157, 5.09598443745173,
              0.990654756560493, 1.43057392853463, 1.32164415364306, 9.82872576524495,
              8.2800915887356, 8.3759266477347]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g1, g2, g3, g4, g5, g6, g7, g8],
        "hx": [],
        "ranges": ranges,
        "markdown": PROBLEM_G07,
        "x": x_best,
        "fx": fx_best
    }


def get_pg08() -> dict:
    """
    Problem G08
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return - (math.sin(2 * math.pi * x[0]) ** 3) * math.sin(2 * math.pi * x[1]) / \
               (x[0] ** 3 * (x[0] + x[1]))

    def g1(*x):
        return x[0] ** 2 - x[1] + 1

    def g2(*x):
        return 1 - x[0] + (x[1] - 4) ** 2

    ranges = [[0, 10], [0, 10]]

    x_best = [1.22797135260752599, 4.24537336612274885]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g1, g2],
        "hx": [],
        "ranges": ranges,
        "markdown": PROBLEM_G08,
        "x": x_best,
        "fx": fx_best
    }


def get_pg09() -> dict:
    """
    Problem G09
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return (x[0] - 10) ** 2 + 5 * (x[1] - 12) ** 2 + x[2] ** 4 + 3 * (x[3] - 11) ** 2 + \
               10 * x[4] ** 6 + 7 * x[5] ** 2 + x[6] ** 4 - 4 * x[5] * x[6] - 10 * x[5] - 8 * x[6]

    def g1(*x):
        return - 127 + 2 * x[0] ** 2 + 3 * x[1] ** 4 + x[2] + 4 * x[3] ** 2 + 5 * x[4]

    def g2(*x):
        return - 282 + 7 * x[0] + 3 * x[1] + 10 * x[2] ** 2 + x[3] - x[4]

    def g3(*x):
        return - 196 + 23 * x[0] + x[1] ** 2 + 6 * x[5] ** 2 - 8 * x[6]

    def g4(*x):
        return 4 * x[0] ** 2 + x[1] ** 2 - 3 * x[0] * x[1] + 2 * x[2] ** 2 + 5 * x[5] - 11 * x[6]

    ranges = [[-10, 10] for _ in range(7)]

    x_best = [2.33049935147405174, 1.95137236847114592, -0.477541399510615805,
              4.36572624923625874, -0.624486959100388983, 1.03813099410962173,
              1.5942266780671519]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g1, g2, g3, g4],
        "hx": [],
        "ranges": ranges,
        "markdown": PROBLEM_G09,
        "x": x_best,
        "fx": fx_best
    }


def get_pg10() -> dict:
    """
    Problem G10
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return x[0] + x[1] + x[2]

    def g1(*x):
        return - 1 + 0.0025 * (x[3] + x[5])

    def g2(*x):
        return - 1 + 0.0025 * (x[4] + x[6] - x[3])

    def g3(*x):
        return - 1 + 0.01 * (x[7] - x[4])

    def g4(*x):
        return - x[0] * x[5] + 833.33252 * x[3] + 100 * x[0] - 83333.333

    def g5(*x):
        return - x[1] * x[6] + 1250 * x[4] + x[1] * x[3] - 1250 * x[3]

    def g6(*x):
        return - x[2] * x[7] + 1250000 + x[2] * x[4] - 2500 * x[4]

    ranges = [[100, 10000], [1000, 10000], *[[10, 1000] for _ in range(5)]]

    x_best = [579.306685017979589, 1359.97067807935605, 5109.97065743133317, 182.01769963061534,
              295.601173702746792, 217.982300369384632, 286.41652592786852, 395.601173702746735]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g1, g2, g3, g4, g5, g6],
        "hx": [],
        "ranges": ranges,
        "markdown": PROBLEM_G10,
        "x": x_best,
        "fx": fx_best
    }


def get_pg11() -> dict:
    """
    Problem G11
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return x[0] ** 2 + (x[1] - 1) ** 2

    def h1(*x):
        return x[1] - x[0] ** 2

    ranges = [[-1, 1], [-1, 1]]

    x_best = [-0.707036070037170616, 0.500000004333606807,
              0.707036070037170616, 0.500000004333606807]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [],
        "hx": [h1],
        "ranges": ranges,
        "markdown": PROBLEM_G11,
        "x": x_best,
        "fx": fx_best
    }


def get_pg12() -> dict:
    """
    Problem G12
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return - (100 - (x[0] - 5) ** 2 - (x[1] - 5) ** 2 - (x[2] - 5) ** 2) / 100

    def g1(*x):
        return min([(x[0] - p) ** 2 + (x[1] - q) ** 2 + (x[2] - r) ** 2 - 0.0625
                    for p in range(1, 10)
                    for q in range(1, 10)
                    for r in range(1, 10)])

    ranges = [[0, 10] for _ in range(3)]

    x_best = [5, 5, 5]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g1],
        "hx": [],
        "ranges": ranges,
        "markdown": PROBLEM_G12,
        "x": x_best,
        "fx": fx_best
    }


def get_pg13() -> dict:
    """
    Problem G13
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return math.exp(reduce(lambda a, b: a * b, x))

    def h1(*x):
        return sum([xi ** 2 for xi in x]) - 10

    def h2(*x):
        return x[1] * x[2] - 5 * x[3] * x[4]

    def h3(*x):
        return x[0] ** 3 + x[1] ** 3 + 1

    ranges = [[-2.3, 2.3], [-2.3, 2.3], *[[-3.2, 3.2] for _ in range(3)]]

    x_best = [-1.71714224003, 1.59572124049468, 1.8272502406271,
              -0.763659881912867, -0.76365986736498]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [],
        "hx": [h1, h2, h3],
        "ranges": ranges,
        "markdown": PROBLEM_G13,
        "x": x_best,
        "fx": fx_best
    }


def get_pg14() -> dict:
    """
    Problem G14
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return sum([x[i] * (PROBLEM_G14_PARAMETERS[i] + math.log(x[i] / sum(x))) for i in range(len(x))])

    def h1(*x):
        return x[0] + 2 * x[1] + 2 * x[2] + x[5] + x[9] - 2

    def h2(*x):
        return x[3] + 2 * x[4] + x[5] + x[6] - 1

    def h3(*x):
        return x[2] + x[6] + x[7] + 2 * x[8] + x[9] - 1

    ranges = [[10**-4, 10] for _ in range(10)]

    x_best = [0.0406684113216282, 0.147721240492452, 0.783205732104114, 0.00141433931889084,
              0.485293636780388, 0.000693183051556082, 0.0274052040687766, 0.0179509660214818,
              0.0373268186859717, 0.0968844604336845]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [],
        "hx": [h1, h2, h3],
        "ranges": ranges,
        "markdown": PROBLEM_G14,
        "x": x_best,
        "fx": fx_best
    }


def get_pg15() -> dict:
    """
    Problem G15
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return 1000 - x[0] ** 2 - 2 * x[1] ** 2 - x[2] ** 2 - x[0] * x[1] - x[0] * x[2]

    def h1(*x):
        return x[0] ** 2 + x[1] ** 2 + x[2] ** 2 - 25

    def h2(*x):
        return 8 * x[0] + 14 * x[1] + 7 * x[2] - 56

    ranges = [[0, 10] for _ in range(3)]

    x_best = [3.51212812611795133, 0.216987510429556135, 3.55217854929179921]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [],
        "hx": [h1, h2],
        "ranges": ranges,
        "markdown": PROBLEM_G15,
        "x": x_best,
        "fx": fx_best
    }


def get_problem_g16_parameters(*x) -> dict:
    """
    Get Problem G16 parameters
    :return dict: Parameters
    """
    y1 = x[1] + x[2] + 41.6
    c1 = 0.024 * x[3] - 4.62
    y2 = 12.5 / c1 + 12
    c2 = 0.0003535 * (x[0]**2) + 0.5311 * x[0] + 0.08705 * y2 * x[0]
    c3 = 0.052 * x[0] + 78 + 0.002377 * y2 * x[0]
    y3 = c2 / c3
    y4 = 19 * y3
    c4 = 0.04782 * (x[0] - y3) + 0.1956 * (x[0] - y3)**2 / x[1] + 0.6376 * y4 + 1.594 * y3
    c5 = 100 * x[1]
    c6 = x[0] - y3 - y4
    c7 = 0.950 - c4 / c5
    y5 = c6 * c7
    y6 = x[0] - y5 - y4 - y3
    c8 = (y5 + y4) * 0.995
    y7 = c8 / y1
    y8 = c8 / 3798
    c9 = y7 - 0.0663 * y7 / y8 - 0.3153
    y9 = 96.82 / c9 + 0.321 * y1
    y10 = 1.29 * y5 + 1.258 * y4 + 2.29 * y3 + 1.71 * y6
    y11 = 1.71 * x[0] - 0.452 * y4 + 0.580 * y3
    c10 = 12.3 / 752.3
    c11 = (1.75 * y2) * (0.995 * x[0])
    c12 = 0.995 * y10 + 1998
    y12 = c10 * x[0] + c11 / c12
    y13 = c12 - 1.75 * y2
    y14 = 3623 + 64.4 * x[1] + 58.4 * x[2] + 146312 / (y9 + x[4])
    c13 = 0.995 * y10 + 60.8 * x[1] + 48 * x[3] - 0.1121 * y14 - 5095
    y15 = y13 / c13
    y16 = 148000 - 331000 * y15 + 40 * y13 - 61 * y15 * y13
    c14 = 2324 * y10 - 28740000 * y2
    y17 = 14130000 - 1328 * y10 - 531 * y11 + c14 / c12
    c15 = y13 / y15 - y13 / 0.52
    c16 = 1.104 - 0.72 * y15
    c17 = y9 + x[4]
    return {"y1": y1, "c1": c1, "y2": y2, "c2": c2, "c3": c3, "y3": y3, "y4": y4, "c4": c4, "c5": c5, "c6": c6,
            "c7": c7, "y5": y5, "y6": y6, "c8": c8, "y7": y7, "y8": y8, "c9": c9, "y9": y9, "y10": y10,
            "y11": y11, "c10": c10, "c11": c11, "c12": c12, "y12": y12, "y13": y13, "y14": y14, "c13": c13,
            "y15": y15, "y16": y16, "c14": c14, "y17": y17, "c15": c15, "c16": c16, "c17": c17}


def get_pg16() -> dict:
    """
    Problem G16
    :return dict: Returns problem parameters
    """

    def objective_function(*x):
        cnt = get_problem_g16_parameters(*x)
        return (0.000117 * cnt["y14"] + 0.1365 + 0.00002358 * cnt["y13"] + 0.000001502 * cnt["y16"] +
                0.0321 * cnt["y12"] + 0.004324 * cnt["y5"] + 0.0001 * cnt["c15"] / cnt["c16"] +
                37.84 * cnt["y2"] / cnt["c12"] - 0.0000005843 * cnt["y17"])

    def g1(*x):
        cnt = get_problem_g16_parameters(*x)
        return (0.28 / 0.72) * cnt["y5"] - cnt["y4"]

    def g2(*x):
        cnt = get_problem_g16_parameters(*x)
        return x[2] - 1.5 * x[1]

    def g3(*x):
        cnt = get_problem_g16_parameters(*x)
        return 3496 * cnt["y2"] / cnt["c12"] - 21

    def g4(*x):
        cnt = get_problem_g16_parameters(*x)
        return 110.6 + cnt["y1"] - 62212 / cnt["c17"]

    def g5(*x):
        cnt = get_problem_g16_parameters(*x)
        return 213.1 - cnt["y1"]

    def g6(*x):
        cnt = get_problem_g16_parameters(*x)
        return cnt["y1"] - 405.23

    def g7(*x):
        cnt = get_problem_g16_parameters(*x)
        return 17.505 - cnt["y2"]

    def g8(*x):
        cnt = get_problem_g16_parameters(*x)
        return cnt["y2"] - 1053.6667

    def g9(*x):
        cnt = get_problem_g16_parameters(*x)
        return 11.275 - cnt["y3"]

    def g11(*x):
        cnt = get_problem_g16_parameters(*x)
        return 214.228 - cnt["y4"]

    def g12(*x):
        cnt = get_problem_g16_parameters(*x)
        return cnt["y4"] - 665.585

    def g13(*x):
        cnt = get_problem_g16_parameters(*x)
        return 7.458 - cnt["y5"]

    def g14(*x):
        cnt = get_problem_g16_parameters(*x)
        return cnt["y5"] - 584.463

    def g15(*x):
        cnt = get_problem_g16_parameters(*x)
        return 0.961 - cnt["y6"]

    def g16(*x):
        cnt = get_problem_g16_parameters(*x)
        return cnt["y6"] - 265.916

    def g10(*x):
        cnt = get_problem_g16_parameters(*x)
        return cnt["y3"] - 35.03

    def g17(*x):
        cnt = get_problem_g16_parameters(*x)
        return 1.612 - cnt["y7"]

    def g18(*x):
        cnt = get_problem_g16_parameters(*x)
        return cnt["y7"] - 7.046

    def g19(*x):
        cnt = get_problem_g16_parameters(*x)
        return 0.146 - cnt["y8"]

    def g20(*x):
        cnt = get_problem_g16_parameters(*x)
        return cnt["y8"] - 0.222

    def g21(*x):
        cnt = get_problem_g16_parameters(*x)
        return 107.99 - cnt["y9"]

    def g22(*x):
        cnt = get_problem_g16_parameters(*x)
        return cnt["y9"] - 273.366

    def g23(*x):
        cnt = get_problem_g16_parameters(*x)
        return 922.693 - cnt["y10"]

    def g24(*x):
        cnt = get_problem_g16_parameters(*x)
        return cnt["y10"] - 1286.105

    def g25(*x):
        cnt = get_problem_g16_parameters(*x)
        return 926.832 - cnt["y11"]

    def g26(*x):
        cnt = get_problem_g16_parameters(*x)
        return cnt["y11"] - 1444.046

    def g27(*x):
        cnt = get_problem_g16_parameters(*x)
        return 18.766 - cnt["y12"]

    def g28(*x):
        cnt = get_problem_g16_parameters(*x)
        return cnt["y12"] - 537.141

    def g29(*x):
        cnt = get_problem_g16_parameters(*x)
        return 1072.163 - cnt["y13"]

    def g30(*x):
        cnt = get_problem_g16_parameters(*x)
        return cnt["y13"] - 3247.039

    def g31(*x):
        cnt = get_problem_g16_parameters(*x)
        return 8961.448 - cnt["y14"]

    def g32(*x):
        cnt = get_problem_g16_parameters(*x)
        return cnt["y14"] - 26844.086

    def g33(*x):
        cnt = get_problem_g16_parameters(*x)
        return 0.063 - cnt["y15"]

    def g34(*x):
        cnt = get_problem_g16_parameters(*x)
        return cnt["y15"] - 0.386

    def g35(*x):
        cnt = get_problem_g16_parameters(*x)
        return 71084.33 - cnt["y16"]

    def g36(*x):
        cnt = get_problem_g16_parameters(*x)
        return - 140000 + cnt["y16"]

    def g37(*x):
        cnt = get_problem_g16_parameters(*x)
        return 2802713 - cnt["y17"]

    def g38(*x):
        cnt = get_problem_g16_parameters(*x)
        return cnt["y17"] - 12146108

    ranges = [[704.4148, 906.3855], [68.6, 288.88], [0, 134.75], [193, 287.0966], [25, 84.1988]]

    x_best = [705.174537070090537, 68.5999999999999943, 102.899999999999991,
              282.324931593660324, 37.5841164258054832]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10,
               g11, g12, g13, g14, g15, g16, g17, g18, g19, g20,
               g21, g22, g23, g24, g25, g26, g27, g28, g29, g30,
               g31, g32, g33, g34, g35, g36, g37, g38],
        "hx": [],
        "ranges": ranges,
        "markdown": PROBLEM_G16,
        "x": x_best,
        "fx": fx_best
    }


def get_pg17() -> dict:
    """
    Problem G17
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        f1 = 30 * x[0] * (0 <= x[0] < 300) + 31 * x[0] * (300 <= x[0] < 400)
        f2 = 28 * x[1] * (0 <= x[1] < 100) + 29 * x[1] * (100 <= x[1] < 200) + 30 * x[1] * (200 <= x[1] < 1000)
        return f1 + f2

    def h1(*x):
        return - x[0] + 300 - math.cos(1.48477 - x[5]) * (x[2] * x[3]) / 131.078 + \
               math.cos(1.47588) * (0.90798 * x[2] ** 2) / 131.078

    def h2(*x):
        return - x[1] - math.cos(1.48477 + x[5]) * (x[2] * x[3]) / 131.078 + \
               math.cos(1.47588) * (0.90798 * x[3] ** 2) / 131.078

    def h3(*x):
        return - x[4] - math.cos(1.48477 + x[5]) * (x[2] * x[3]) / 131.078 + \
               math.sin(1.47588) * (0.90798 * x[3] ** 2) / 131.078

    def h4(*x):
        return 200 - math.sin(1.48477 - x[5]) * (x[2] * x[3]) / 131.078 + \
               math.sin(1.47588) * (0.90798 * x[2] ** 2) / 131.078

    ranges = [[0, 400], [0, 1000], [340, 420], [340, 420], [-1000, 1000]]

    x_best = [201.784467214523659, 99.9999999999999005, 383.071034852773266,
              420.0, -10.9076584514292652, 0.0731482312084287128]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [],
        "hx": [h1, h2, h3, h4],
        "ranges": ranges,
        "markdown": PROBLEM_G17,
        "x": x_best,
        "fx": fx_best
    }


def get_pg18() -> dict:
    """
    Problem G18
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return - 0.5 * (x[0] * x[3] - x[1] * x[2] + x[2] * x[8] - x[4] * x[8] +
                        x[4] * x[7] - x[5] * x[6])

    def g1(*x):
        return x[2]**2 + x[3]**2 - 1

    def g2(*x):
        return x[8]**2 - 1

    def g3(*x):
        return x[4]**2 + x[5]**2 - 1

    def g4(*x):
        return x[0]**2 + (x[1] - x[8])**2 - 1

    def g5(*x):
        return (x[0] - x[4])**2 + (x[1] - x[5])**2 - 1

    def g6(*x):
        return (x[0] - x[6])**2 + (x[1] - x[7])**2 - 1

    def g7(*x):
        return (x[2] - x[4])**2 + (x[3] - x[5])**2 - 1

    def g8(*x):
        return (x[2] - x[6])**2 + (x[3] - x[7])**2 - 1

    def g9(*x):
        return x[6]**2 + (x[7] - x[8])**2 - 1

    def g10(*x):
        return x[1] * x[2] - x[0] * x[3]

    def g11(*x):
        return - x[2] * x[8]

    def g12(*x):
        return x[4] * x[8]

    def g13(*x):
        return x[5] * x[6] - x[4] * x[7]

    ranges = [*[[-10, 10] for _ in range(8)], [0, 20]]

    x_best = [-0.657776192427943163, -0.153418773482438542, 0.323413871675240938,
              -0.946257611651304398, -0.657776194376798906, -0.753213434632691414,
              0.323413874123576972, -0.346462947962331735, 0.59979466285217542]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13],
        "hx": [],
        "ranges": ranges,
        "markdown": PROBLEM_G18,
        "x": x_best,
        "fx": fx_best
    }


def get_pg19() -> dict:
    """
    Problem G19
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return sum([PROBLEM_G19_PARAMETERS["c"][i][j] * x[10+i] * x[10+j]
                    for i in range(5) for j in range(5)]) +\
               2 * sum([PROBLEM_G19_PARAMETERS["d"][j] * x[10+j]**3 for j in range(5)]) -\
               sum([PROBLEM_G19_PARAMETERS["b"][i] * x[i] for i in range(10)])

    def g(j):
        def gj(*x):
            return - 2 * sum([PROBLEM_G19_PARAMETERS["c"][i][j] * x[10+i] for i in range(5)])\
                   - 3 * PROBLEM_G19_PARAMETERS["d"][j] * x[10+j]**2\
                   - PROBLEM_G19_PARAMETERS["e"][j]\
                   + sum([PROBLEM_G19_PARAMETERS["a"][i][j] * x[i] for i in range(10)])
        return gj

    ranges = [*[[0, 10] for _ in range(15)]]

    x_best = [1.66991341326291344 * 10**-17, 3.95378229282456509 * 10**-16,
              3.94599045143233784, 1.06036597479721211 * 10**-16, 3.2831773458454161,
              9.99999999999999822, 1.12829414671605333 * 10**- 17,
              1.2026194599794709 * 10**-17, 2.50706276000769697 * 10**-15,
              2.24624122987970677 * 10**-15, 0.370764847417013987, 0.278456024942955571,
              0.523838487672241171, 0.388620152510322781, 0.298156764974678579]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g(j) for j in range(5)],
        "hx": [],
        "ranges": ranges,
        "markdown": PROBLEM_G19,
        "x": x_best,
        "fx": fx_best
    }


def get_pg20() -> dict:
    """
    Problem G20
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return sum([PROBLEM_G20_PARAMETERS["a"][i] * x[i] for i in range(24)])

    def gi1(i):
        def gi(*x):
            return (x[i] + x[i+12]) / (sum(x) + PROBLEM_G20_PARAMETERS["e"][i])
        return gi

    def gi2(i):
        def gi(*x):
            return (x[i+3] + x[i+15]) / (sum(x) + PROBLEM_G20_PARAMETERS["e"][i])
        return gi

    def h(i):
        def hi(*x):
            return x[i+12] / (
                    PROBLEM_G20_PARAMETERS["b"][i+12] *
                    sum([x[j]/PROBLEM_G20_PARAMETERS["b"][j] for j in range(12, 24)])
            ) - (PROBLEM_G20_PARAMETERS["c"][i] * x[i]) / (
                    40 * PROBLEM_G20_PARAMETERS["b"][i] *
                    sum([x[j] / PROBLEM_G20_PARAMETERS["b"][j] for j in range(12)]))
        return hi

    def h13(*x):
        return sum(x) - 1

    def h14(*x):
        return sum([x[i] / PROBLEM_G20_PARAMETERS["d"][i] for i in range(12)]) +\
               PROBLEM_G20_PARAMETERS["k"] * sum([x[i] / PROBLEM_G20_PARAMETERS["b"][i]
                                                  for i in range(12, 24)]) - 1.671

    ranges = [*[[0, 10] for _ in range(24)]]

    x_best = [1.28582343498528086 * 10**-18, 4.83460302526130664 * 10**-34, 0, 0,
              6.30459929660781851 * 10**-18, 7.57192526201145068 * 10**-34,
              5.03350698372840437 * 10**-34, 9.28268079616618064 * 10**-34, 0,
              1.76723384525547359 * 10**-17, 3.55686101822965701 * 10**-34,
              2.99413850083471346 * 10**-34, 0.158143376337580827, 2.29601774161699833 * 10**-19,
              1.06106938611042947 * 10**-18, 1.31968344319506391 * 10**-18, 0.530902525044209539,
              0, 2.89148310257773535 * 10**-18, 3.34892126180666159 * 10**-18, 0,
              0.310999974151577319, 5.41244666317833561 * 10**-5, 4.84993165246959553 * 10**-16]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [*[gi1(i) for i in range(3)], *[gi2(i) for i in range(3, 6)]],
        "hx": [*[h(i) for i in range(12)], h13, h14],
        "ranges": ranges,
        "markdown": PROBLEM_G20,
        "x": x_best,
        "fx": fx_best
    }


def get_pg21() -> dict:
    """
    Problem G21
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return x[0]

    def g1(*x):
        return - x[0] + 35 * x[1]**0.6 + 35 * x[2]**0.6

    def h1(*x):
        return - 300 * x[2] + 7500 * x[4] - 7500 * x[5] - 25 * x[3] * x[4] +\
               25 * x[3] * x[5] + x[2] * x[3]

    def h2(*x):
        return 100 * x[1] + 155.365 * x[3] + 2500 * x[6] - x[1] * x[3] -\
               25 * x[3] * x[6] - 15536.5

    def h3(*x):
        return - x[4] + math.log(- x[3] + 900)

    def h4(*x):
        return - x[5] + math.log(x[3] + 300)

    def h5(*x):
        return - x[6] + math.log(- 2 * x[3] + 700)

    ranges = [[0, 1000], [0, 40], [0, 40], [100, 300], [6.3, 6.7], [5.9, 6.4], [4.5, 6.25]]

    x_best = [193.724510070034967, 5.56944131553368433 * 10**-27,
              17.3191887294084914, 100.047897801386839, 6.68445185362377892,
              5.99168428444264833, 6.21451648886070451]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g1],
        "hx": [h1, h2, h3, h4, h5],
        "ranges": ranges,
        "markdown": PROBLEM_G21,
        "x": x_best,
        "fx": fx_best
    }


def get_pg22() -> dict:
    """
    Problem G22
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return x[0]

    def g1(*x):
        return - x[0] + x[1] ** 0.6 + x[2] + x[3]

    def h1(*x):
        return x[4] - 100000 * x[7] + 10 ** 7

    def h2(*x):
        return x[5] + 100000 * x[7] - 100000 * x[8]

    def h3(*x):
        return x[6] + 100000 * x[8] - 5 * 10 ** 7

    def h4(*x):
        return x[4] + 100000 * x[9] - 3.3 * 10 ** 7

    def h5(*x):
        return x[5] + 100000 * x[10] - 4.4 * 10 ** 7

    def h6(*x):
        return x[6] + 100000 * x[11] - 6.6 * 10 ** 7

    def h7(*x):
        return x[4] - 120 * x[1] * x[12]

    def h8(*x):
        return x[5] - 80 * x[2] * x[13]

    def h9(*x):
        return x[6] - 40 * x[3] * x[14]

    def h10(*x):
        return x[7] - x[10] + x[15]

    def h11(*x):
        return x[8] - x[11] + x[16]

    def h12(*x):
        return - x[17] + math.log(x[9] - 100)

    def h13(*x):
        return - x[18] + math.log(-x[7] + 300)

    def h14(*x):
        return - x[20] + math.log(x[15])

    def h15(*x):
        return - x[20] + math.log(-x[8] + 400)

    def h16(*x):
        return - x[21] + math.log(x[16])

    def h17(*x):
        return - x[7] - x[9] + x[12] * x[17] - x[12] * x[18] + 400

    def h18(*x):
        return x[7] - x[8] - x[10] + x[13] * x[20] - x[13] * x[20] + 400

    def h19(*x):
        return x[8] - x[11] - 4.60517 * x[14] + x[14] * x[21] + 100

    ranges = [
        [0, 20000], [0, 10**6], [0, 10**6], [0, 10**6],
        [0, 10**7], [0, 10**7], [0, 10**7], [100, 299.99],
        [100, 399.99], [100.01, 300], [100, 400], [100, 600],
        [0, 500], [0, 500], [0, 500], [0.01, 300], [0.01, 400],
        *[[-4.7, 6.25] for _ in range(5)]
    ]

    x_best = [236.430975504001054, 135.82847151732463, 204.818152544824585, 6446.54654059436416,
              3007540.83940215595, 4074188.65771341929, 32918270.5028952882, 130.075408394314167,
              170.817294970528621, 299.924591605478554, 399.258113423595205, 330.817294971142758,
              184.51831230897065, 248.64670239647424, 127.658546694545862, 269.182627528746707,
              160.000016724090955, 5.29788288102680571, 5.13529735903945728, 5.59531526444068827,
              5.43444479314453499, 5.07517453535834395]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g1],
        "hx": [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10,
               h11, h12, h13, h14, h15, h16, h17, h18, h19],
        "ranges": ranges,
        "markdown": PROBLEM_G22,
        "x": x_best,
        "fx": fx_best
    }


def get_pg23() -> dict:
    """
    Problem G23
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return - 9 * x[4] - 15 * x[7] + 6 * x[0] + 16 * x[1] + 10 * (x[5] + x[6])

    def g1(*x):
        return x[8] * x[2] + 0.02 * x[5] - 0.025 * x[4]

    def g2(*x):
        return x[8] * x[3] + 0.02 * x[6] - 0.015 * x[7]

    def h1(*x):
        return x[0] + x[1] - x[2] - x[3]

    def h2(*x):
        return 0.03 * x[0] + 0.01 * x[1] - x[8] * (x[2] + x[3])

    def h3(*x):
        return x[2] + x[5] - x[4]

    def h4(*x):
        return x[3] + x[6] - x[7]

    ranges = [[0, 300], [0, 300], [0, 100], [0, 200], [0, 100],
              [0, 300], [0, 100], [0, 200], [0.01, 0.03]]

    x_best = [0.00510000000000259465, 99.9947000000000514, 9.01920162996045897 * 10**-18,
              99.9999000000000535, 0.000100000000027086086, 2.75700683389584542 * 10**-14,
              99.9999999999999574, 200, 0.0100000100000100008]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g1, g2],
        "hx": [h1, h2, h3, h4],
        "ranges": ranges,
        "markdown": PROBLEM_G23,
        "x": x_best,
        "fx": fx_best
    }


def get_pg24() -> dict:
    """
    Problem G24
    :return dict: Returns problem parameters
    """
    def objective_function(*x):
        return - x[0] - x[1]

    def g1(*x):
        return - 2 * x[0]**4 + 8 * x[0]**3 - 8 * x[0]**2 + x[1] - 2

    def g2(*x):
        return - 4 * x[0]**4 + 32 * x[0]**3 - 88 * x[0]**2 + 96 * x[0] + x[1] - 36

    ranges = [[0, 3], [0, 4]]

    x_best = [2.32952019747762, 3.17849307411774]

    fx_best = objective_function(*x_best)

    return {
        "objective_function": objective_function,
        "gx": [g1, g2],
        "hx": [],
        "ranges": ranges,
        "markdown": PROBLEM_G24,
        "x": x_best,
        "fx": fx_best
    }
