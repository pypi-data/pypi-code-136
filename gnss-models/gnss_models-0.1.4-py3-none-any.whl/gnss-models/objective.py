from numpy import sin


def quadratic_polynomial(x, a, b, c):
    return a * x ** 2 + b * x + c


def cubic_polynomial(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d


def sine_wave(x, a, b, c):
    return a * sin(b * x) + c
