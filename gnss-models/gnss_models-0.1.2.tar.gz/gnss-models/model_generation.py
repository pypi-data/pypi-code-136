import numpy as np

from utils import split_data, split_p_val
from objective import cubic_polynomial
from scipy.optimize import curve_fit


def generate_piecewise_cubic_model(x, y):
    time_min = x.min()
    x = np.array([i - time_min for i in x])
    results = split_data(x, y)

    # Instantiate variables for model
    str_model = [{'correction': time_min}]

    # Instantiate variables for model
    x_vals = []
    y_vals = []

    # Create pieces of the model
    for result in results:
        x_temp = np.array(result[0])
        y_temp = np.array(result[1])

        # Model Piece
        popt, _ = curve_fit(cubic_polynomial, x_temp, y_temp)
        a, b, c, d = popt
        x_min = x_temp[0]
        x_max = x_temp[-1]
        str_model.append(
            {'a': round(a, 2), 'b': round(b, 2), 'c': round(c, 2), 'd': round(d, 2), 'x_min': round(x_min, 6),
             'x_max': round(x_max, 6)})
        x_vals.append((x_min <= x) * (x <= x_max))
        y_vals.append(lambda l=x, m=a, n=b, o=c, p=d: cubic_polynomial(l, m, n, o, p))

    return str_model


def apply_model(p_value, x, y, str_model):
    time_min = str_model[0]['correction']
    x = np.array([i - time_min for i in x])

    intervals = []

    for i in range(1, len(str_model)):
        new_dict = {'x_min': str_model[i]['x_min'], 'x_max': str_model[i]['x_max']}
        intervals.append(new_dict)

    results = split_p_val(p_value, x, y, intervals)

    # Instantiate variables for model
    x_vals = []
    y_vals = []

    # Create pieces of the model
    for result in results:
        x_min = result['x_min'] % p_value
        x_max = result['x_max'] % p_value
        i = 1
        while not (x_min == str_model[i]['x_min']) and (x_max == str_model[i]['x_max'], 1):
            i += 1

        a = str_model[i]['a']
        b = str_model[i]['b']
        c = str_model[i]['c']
        d = str_model[i]['d']
        x_vals.append((x_min < x % p_value) * (x % p_value <= x_max))
        y_vals.append(lambda l=x, m=a, n=b, o=c, p=d: cubic_polynomial(l % p_value, m, n, o, p))

    np_model = np.piecewise(x, x_vals, y_vals)
    return np_model
