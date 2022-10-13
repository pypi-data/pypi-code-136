from cycler import cycler, Cycler
import matplotlib.pyplot as plt
import numpy as np
import warnings

symbols = ['o','d','^','x']
linestyles = ['-','--','-.','.']

def ICIW_colormap_cycler(colormap : str, num_plots : int, start : float = 0.1, stop : float = 0.9) -> Cycler:
    """Generates a color cycler from an given colormap. For available options see :
     https://matplotlib.org/stable/tutorials/colors/colormaps.html

    Parameters
    ----------
    colormap : str
        see https://matplotlib.org/stable/tutorials/colors/colormaps.html
    num_plots : int
        Number of unique colors to sample
    start : float, optional
        lower bound, by default 0.1
    stop : float, optional
        upper bound, by default 0.9

    Returns
    -------
    cycler
        plt.cycler to use in a context manager
    """
    cmap=plt.get_cmap(colormap)
    _cycler= cycler("color", cmap(np.linspace(start,stop,num_plots)))
    return _cycler

def ICIW_symbol_cycler(num_plots : int, sym_list : list[str] = symbols) -> Cycler:
    if num_plots>len(sym_list):
        warnings.warn(f"Attempted to use more unique symbols than in sym_list: \n len:{len(sym_list)} | {sym_list} \n Falling back to using all available symbols.")
        _cycler=cycler("marker",sym_list)
    else:
        _cycler=cycler("marker",sym_list[:num_plots])
    return _cycler

def ICIW_linestyle_cycler(num_plots : int, ls_list : list[str] = linestyles) -> Cycler:
    if num_plots>len(ls_list):
        warnings.warn(f"Attempted to use more unique symbols than in sym_list: \n len:{len(ls_list)} | {ls_list} \n Falling back to using all available symbols.")
        _cycler=cycler("linestyle",ls_list)
    else:
        _cycler=cycler("linestyle",ls_list[:num_plots])
    return _cycler
