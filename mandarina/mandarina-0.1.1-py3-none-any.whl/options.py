import numpy as np


def setup_numpy_print_options():
    np.set_printoptions(
        suppress=True, formatter={"float_kind": "{:0.2f}".format}
    )  # specify numpy print output format
