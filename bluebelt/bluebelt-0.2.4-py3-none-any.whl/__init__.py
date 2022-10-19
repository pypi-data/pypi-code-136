# from bluebelt.core import index
from bluebelt.core import series
from bluebelt.core import dataframe
from bluebelt.core.workload import Workload
from bluebelt.core.forecast import Forecast

from bluebelt.create import create

import bluebelt.styles.rc
from bluebelt.helpers.colors import replace_colors

import os

from cycler import cycler

import matplotlib as mpl
import matplotlib.pyplot as plt

import yaml
import warnings

import copy

class BlueConfig:
    _config = {}

    @staticmethod
    def get(name):
        if name in BlueConfig._config.keys():
            return BlueConfig._config[name]
        elif (
            ".".join(name.split(".")[:-1]) in BlueConfig._config.keys()
        ):  # is the name up to the last dot in keys?
            # is the last part of the name in this valueset?
            if (
                name.split(".")[-1]
                in BlueConfig._config[".".join(name.split(".")[:-1])]
            ):
                return BlueConfig._config[".".join(name.split(".")[:-1])][
                    name.split(".")[-1]
                ]
            else:
                return None
        else:
            return None

    @staticmethod
    def set(name, value):
        BlueConfig._config[name] = value

    @staticmethod
    def default():
        set_style("fat")

def config(key=None, value=None):
    """
    Change or get the Bluebelt configuration.

    Parameters
    ----------
    key: the name of the configuration parameter
    value: the value of the configuration parameter

    Returns
    -------
    If key and value are provided parameter key is set to value and nothing is
    returned.
    If only key is provided the parameter value is returned.
    If key and value are both not provided the configuration is reset to the
    default parameter values.
    """

    if key and value:
        BlueConfig.set(key, value)
    elif key:
        return BlueConfig.get(key)
    else:
        BlueConfig.default()

def style(value=None):
    style = config('style')
    
    if value:
        values = value.split(".")
        for value in values:
            style = style.get(value)

    # check colors

    return style

def set_style(name=None):
    
    path = os.path.dirname(os.path.realpath(__file__))

    # check if name is pointing to a yaml file
    if os.path.splitext(name)[1] not in [".yaml", ".yml"]:
        path_file = f"{path}/styles/{name}.yaml"

        # check if the style exists
        if not os.path.isfile(path_file):

            # list styles
            style_list = ""
            for file in os.listdir(f"{path}/styles/"):
                if file.endswith(".yaml"):
                    if len(style_list) > 0:
                        style_list += ", "
                    style_list += str(file.split(".")[0])
            raise ValueError(
                f"{name} style does not exist. Choose from {str(style_list)}"
            )
    else:
        path_file = name

    try:
        with open(path_file, "r") as file:
            style = yaml.load(file, yaml.SafeLoader)

        # handle the matplotlib rc items in the yaml
        rc = style.pop('rc', {})
        for key, value in rc.items():
            # set the values in matplotlib rcparams
            mpl.rc(key, **value)

        BlueConfig.set('style', style)

        # change the matplotlib color cycle if there are colors in the style
        if style.get('colors', None):
            plt.rc('axes', prop_cycle=(cycler('color', style.get('colors', None))))

    except OSError as e:
        print(f"Unable to find {path_file}. Did you enter the correct file path?")

def set_figsize_in_pixels(
    size: tuple or int = None, height: int = None, dpi: int = None
):
    """
    Set the default figsize in pixels

    Parameters
    ----------
    size : tuple or int, default None
        a tuple with (width, height) values or
        an int with the 'width' value in which case a height must be provided
    height: int, default None
        if size is an int height will complete the figsize
    dpi: int, default None
        change the default dpi (dots per inch, or dots per 2.54 cm)

    Returns
    -------
    None

    Example
    -------
    bluebelt.set_figsize_in_pixels(900, 600)

    """
    # set or get dpi
    if dpi:
        mpl.rcParams["figure.dpi"] = dpi
    else:
        dpi = mpl.rcParams["figure.dpi"]

    # in case two int are passed
    if height and isinstance(size, int):
        size = (size, height)

    # set figsize
    mpl.rcParams["figure.figsize"] = tuple(ti / dpi for ti in size)

def set_figsize_in_cm(size: tuple or int = None, height: int = None, dpi: int = None):
    """
    Set the default figsize in centimeters

    Parameters
    ----------
    size : tuple or int, default None
        a tuple with (width, height) values or
        an int with the 'width' value in which case a height must be provided
    height: int, default None
        if size is an int height will complete the figsize
    dpi: int, default None
        change the default dpi (dots per inch, or dots per 2.54 cm)

    Returns
    -------
    None

    Example
    -------
    bluebelt.set_figsize_in_cm(5, 8)

    """
    # set or get dpi
    if dpi:
        mpl.rcParams["figure.dpi"] = dpi
    else:
        dpi = mpl.rcParams["figure.dpi"]

    # in case two int are passed
    if height and isinstance(size, int):
        size = (size, height)

    # set figsize
    mpl.rcParams["figure.figsize"] = tuple(ti / 2.54 for ti in size)

def set_transparent(transparent: bool = False):
    """
    Set the default way to handle transparency when saving an image.

    Parameters
    ----------
    transparent : bool, default False

    Returns
    -------
    None

    Example
    -------
    bluebelt.set_transparent(True)

    """
    mpl.rcParams["savefig.transparent"] = transparent

def set_drop(drop: bool = True):
    """
    Set the default way to handle dropping data in filters.

    Parameters
    ----------
    drop : bool, default None

    Returns
    -------
    None

    Example
    -------
    bluebelt.set_drop(True)

    """
    BlueConfig.set("drop", drop)

def set_inplace(inplace: bool = True):
    """
    Set the default way to handle inplace operation.

    Parameters
    ----------
    inplace : bool, default None

    Returns
    -------
    None

    Example
    -------
    bluebelt.set_drop(True)

    """
    BlueConfig.set("inplace", inplace)

def set_language(language=None):
    """
    Set the default language.

    Parameters
    ----------
    language : str, default None
        currently only support 'en' and 'nl'
        currently only works for weekday names

    Returns
    -------
    None

    Example
    -------
    bluebelt.set_language('en')

    """
    languages = ["nl", "en"]
    if language not in languages:
        raise ValueError(
            f"The language should be one of {str(languages)[1:-1]}, not {language}."
        )

    BlueConfig.set("language", language)

def set_plotting(plotting: str = 'matplotlib'):
    """
    Set the default plotting backend.

    Parameters
    ----------
    plotting : str, 'matplotlib' or 'plotly', default 'matplotlib'

    Returns
    -------
    None

    Example
    -------
    bluebelt.set_plotting('plotly')

    """
    if plotting == 'plotly' and style('name') == 'paper':
        warnings.warn("'paper' style can not be used with plotly. 'fat' style will be activated.")
        set_style('fat')
    BlueConfig.set("plotting", plotting)

def set_colors(colors: list = None):
    """
    Set the default colors.

    Parameters
    ----------
    colors : list, default []

    Returns
    -------
    None

    Example
    -------
    bluebelt.set_colors(["#ffee00", "#000044"])

    """
    if colors:
        # change the matplotlib color cycle
        plt.rc('axes', prop_cycle=(cycler('color', colors)))

        # replace all the colors in the current style
        config('style', replace_colors(config('style'), colors))
        
set_style("fat")
set_plotting("matplotlib")
set_language("en")
set_drop()
set_inplace()
set_transparent()
