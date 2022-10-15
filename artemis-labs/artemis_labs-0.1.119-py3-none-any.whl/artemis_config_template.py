# pylint: disable=duplicate-code

'''
This custom config file is where you can create output anchors,
customize your runtime settings, customize your runtime information,
and register custom fields.
'''

# pylint: disable=line-too-long
# pylint: disable=too-many-branches
# pylint: disable=pointless-string-statement
# pylint: disable=unused-argument
# pylint: disable=self-assigning-variable
# pylint: disable=invalid-name
# pylint: disable=unused-import

import sys
import datetime
import io
import inspect
import base64
import typing
from typing import List, Dict, Any, Tuple

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# ========================================================
# Artemis Imports
# ========================================================
from artemis_labs.artemis_helper import ArtemisHelper, ArtemisType
from artemis_labs.artemis_config_manager import ArtemisConfigManager
from artemis_labs.artemis_runtime_manager import ArtemisRuntimeManager

# ========================================================
# WARNING: DO NOT EDIT
def setup_plot_args(named_args_dict : Dict) -> None:
    '''
    Uses dictionary of named_args_dict to customize matplotlib graph
    :param named_args_dict: Dictionary of named args
    :return: None
    '''

    # Graph parameters
    xmin = None
    xmax = None
    ymin = None
    ymax = None
    figsize = (8,3)
    xlabel = ""
    ylabel = ""
    title = ""

    # Run args
    if 'xmin' in named_args_dict:
        xmin = float(named_args_dict['xmin'])
    if 'xmax' in named_args_dict:
        xmax = float(named_args_dict['xmax'])
    if 'ymin' in named_args_dict:
        ymin = float(named_args_dict['ymin'])
    if 'ymax' in named_args_dict:
        ymax = float(named_args_dict['ymax'])
    if 'xlabel' in named_args_dict:
        xlabel = named_args_dict['xlabel']
    if 'ylabel' in named_args_dict:
        ylabel = named_args_dict['ylabel']
    if 'title' in named_args_dict:
        title = named_args_dict['title']
    if 'figsize' in named_args_dict:
        figsize_input = named_args_dict['figsize'].replace(')', '').replace('(', '')
        figsize_components = figsize_input.split(',')
        figsize = (float(figsize_components[0]), float(figsize_components[1]))

    # Make plot
    plt.figure(figsize=figsize)

    # Set limits
    if xmin is not None:
        plt.xlim(left=xmin)
    if xmax is not None:
        plt.xlim(right=xmax)
    if ymax is not None:
        plt.ylim(top = ymax)
    if ymin is not None:
        plt.ylim(bottom=ymin)

    # Set labels
    if xlabel != '':
        plt.xlabel(xlabel)
    if ylabel != '':
        plt.ylabel(ylabel)

    # Set title
    if title != '':
        plt.title(title)
# ========================================================

# ========================================================
# Run Information and Fields
# ========================================================

# Custom run information
run_information = {
    'Field 1' : 'Value'
}
ArtemisRuntimeManager.register_run_information(run_information)

# Custom fields
fields = {
    'custom' : '123ABC',
}
ArtemisRuntimeManager.register_fields(fields)

# Custom runtime settings
runtime_settings = {
    'delay' : 0
}
ArtemisRuntimeManager.register_runtime_settings(runtime_settings)

# ========================================================
# Custom Anchors
# ========================================================

# Example Custom Anchor 1
def scatter_graph(arr , named_args_dict : Dict) -> Tuple:
    '''
    This takes in a container of numerical values and named args,
    plots a scatter plot using those numerical values, using
    named arguments to customize the graph,
    and returns a serialized form of the matplotlib figure
    :param arr: Container of values to graph (List or Numpy)
    :param named_args_dict: Named arguments provided when invoking decorator
    :return: Serialized scatter graph
    '''

    # Setup plot arguments
    setup_plot_args(named_args_dict)

    # Check if we are using data-x data-y mode
    if 'data-x' in named_args_dict and 'data-y' in named_args_dict:

        # Get arrays
        arr_x = named_args_dict['data-x']
        arr_y = named_args_dict['data-y']

        # Convert
        arr_x = ArtemisHelper.convert_if(arr_x, ArtemisType.LIST, ArtemisType.NUMPY_ARRAY)
        arr_y = ArtemisHelper.convert_if(arr_y, ArtemisType.LIST, ArtemisType.NUMPY_ARRAY)

        # Check dimensionaliy
        ArtemisHelper.assert_true(arr_x.ndim == 1)
        ArtemisHelper.assert_true(arr_y.ndim == 1)

        # Actually plot data
        plt.scatter(arr_x, arr_y)
    else:

        # Convert type to numpy array if it is a list
        arr = ArtemisHelper.convert_if(arr, ArtemisType.LIST, ArtemisType.NUMPY_ARRAY)

        # Validate input
        ArtemisHelper.assert_input_is_type(arr, np.ndarray)

        # Reshape data for line plot
        if arr.ndim == 2:
            if arr.shape[1] == 2:
                arr = arr
            elif arr.shape[0] == 2:
                arr = np.array(list(zip(arr[0], arr[1])))
            else:
                return None

        # Actually plot data
        if arr.ndim == 2:
            plt.scatter(arr[:,0], arr[:,1])

    # Serialize plot
    serialized_plot = ArtemisHelper.serialize(None, ArtemisType.MATPLOTLIB_PLOT, named_args_dict)

    # Close figure
    plt.close()

    # Return serialized plot
    return serialized_plot
ArtemisConfigManager.register_function(scatter_graph, 'scatter-graph')

# Example Custom Anchor 2
def histogram(arr , named_args_dict : Dict) -> Tuple:
    '''
    This takes in a 1D container of numerical values and named args,
    plots a histogram using those numerical values, using
    named arguments to customize the graph,
    and returns a serialized form of the matplotlib figure
    :param arr: 1D container of values to graph (List or Numpy)
    :param named_args_dict: Named arguments provided when invoking decorator
    :return: Serialized histogram
    '''

    # Convert type to numpy array if it is a list
    arr = ArtemisHelper.convert_if(arr, ArtemisType.LIST, ArtemisType.NUMPY_ARRAY)

    # Validate input
    ArtemisHelper.assert_input_is_type(arr, np.ndarray)

    # Setup plot arguments
    setup_plot_args(named_args_dict)

    # Actually plot data
    plt.hist(arr, 50)

    # Serialize plot
    serialized_plot = ArtemisHelper.serialize(None, ArtemisType.MATPLOTLIB_PLOT, named_args_dict)

    # Close figure
    plt.close()

    # Return serialized plot
    return serialized_plot
ArtemisConfigManager.register_function(histogram, 'histogram')
