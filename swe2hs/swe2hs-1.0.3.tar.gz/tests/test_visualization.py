from swe2hs.one_dimensional import convert_1d
import pytest
import numpy as np
import pandas as pd

import matplotlib as mpl
mpl.use('agg')
import matplotlib.pyplot as plt

from swe2hs.visualization import (
    groupby_hydroyear,
    layer_plot,
    )


def test_layer_plot(valid_swe_sample_data):
    """
    Only test if function works withot error. No validation if everything is
    correct.
    """
    result = convert_1d(valid_swe_sample_data, return_layers=True)

    fig, ax = plt.subplots()
    layer_plot(ax, result)
    plt.close()

    for y, d in groupby_hydroyear(result):
        fig, ax = plt.subplots()
        layer_plot(ax, d)
        plt.close()

    fig, ax = plt.subplots()
    layer_plot(ax, result, color_variable=None)
    plt.close()

    for y, d in groupby_hydroyear(result):
        fig, ax = plt.subplots()
        layer_plot(ax, d, color_variable=None)
        plt.close()

