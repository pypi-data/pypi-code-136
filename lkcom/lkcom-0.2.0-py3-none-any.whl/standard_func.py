"""lkcom - a Python library of useful routines.

This module contains various standard mathematical functions.

Copyright 2015-2022 Lukas Kontenis
Contact: dse.ssd@gmail.com
"""
import numpy as np
import matplotlib.pyplot as plt

from lkcom.util import get_color

def gaussian_1D(X=None, A=1, w=None, c=None, y0=0, sigma=None):
    """Evaluate a 1D Gaussian."""
    if X is None:
        sz = 100
        X = np.arange(0, sz, 1, float)
    else:
        sz = len(X)

    if w is None:
        w = sz/5

    if c is None:
        c = sz/2

    if sigma is None:
        sigma = w/np.sqrt(8*np.log(2))

    return A*np.exp(-(X-c)**2/(2*sigma**2)) + y0


def gaussian_1D_arglist(args, X=None):
    """Evaluate a 1D Gaussian"""
    return gaussian_1D(X, A=args[0], w=args[1], c=args[2], y0=args[3])


def plot_gaussian_1D(
        X=None, A=1, width=None, center=None, y0=0,
        c=get_color('r'), ls='-', ls_markers='--'):
    """
    Plot a nice 1D Gaussian.
    """
    if X is None:
        X = np.arange(0, 100)

    sz = len(X)

    if width is None:
        width = sz/10

    if center is None:
        center = sz/2

    Y = gaussian_1D(X, A=A, w=width, c=center, y0=y0)
    plt.plot(X, Y, c=c, ls=ls)

    w_X = np.array([-1., 1.])*width/2 + center
    w_Y = np.array([1., 1.])*A/2 + y0
    plt.plot(w_X, w_Y, c=c, ls=ls_markers)

    c_X = np.array([1, 1])*center
    c_Y = np.array([y0, A+y0])

    plt.plot(c_X, c_Y, c=c, ls=ls_markers)

    plt.plot([np.min(X), np.max(X)], [y0, y0], c=c, ls=ls_markers)


def plot_gaussian_1D_arglist(args, X=None, **kwargs):
    """Plot a 1D Gaussian."""
    return plot_gaussian_1D(
        X, A=args[0], width=args[1], center=args[2], y0=args[3], **kwargs)
