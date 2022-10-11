from itertools import combinations, combinations_with_replacement
from typing import Optional, Sequence, Union, overload

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure


def _hist(
    data: np.ndarray,
    axis: Axes,
    label: str,
    color: tuple[float, float, float],
) -> None:
    weights = np.ones_like(data)
    weights /= data.shape[0]
    axis.hist(
        data,
        bins=[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        weights=weights,
        color=color,
    )
    axis.text(x=0.02, y=0.98, s=label, size="large", ha="left", va="top")


def _scattercomp(
    data: np.ndarray,
    axis: Axes,
    labels: tuple[str, str],
    color: tuple[float, float, float],
    color_ml: tuple[float, float, float],
    color_dl: tuple[float, float, float],
    opacity: Optional[np.ndarray] = None,
) -> None:
    n_datasets = data[0].shape[0]
    colors = np.zeros((n_datasets, 4))
    colors[:, :3] = color
    colors[:, 3] = opacity if opacity is not None else 1.0

    # draw scatterplot
    axis.scatter(data[0, :], data[1, :], c=colors)

    # draw diagonal auxiliary lines
    axis.plot(
        [0, 1], [0, 1],
        transform=axis.transAxes,
        color=color_dl,
        ls="--",
    )
    axis.plot(
        [0.05, 1], [0, 0.95],
        [0, 0.95], [0.05, 1],
        transform=axis.transAxes,
        color=color_dl+(0.3, ),
        ls="--",
    )

    # draw lines for the mean values on each axis
    mean1 = data[0].mean()
    mean2 = data[1].mean()
    opacity1, ls1 = (0.8, "-") if mean1 > mean2 else (0.5, "--")
    opacity2, ls2 = (0.8, "-") if mean2 > mean1 else (0.5, "--")
    axis.axhline(
        mean2,
        xmin=0,
        xmax=mean2,
        color=color_ml+(opacity2, ),
        ls=ls2,
    )
    axis.axvline(
        mean1,
        ymin=0,
        ymax=mean1,
        color=color_ml+(opacity1, ),
        ls=ls1,
    )
    axis.text(0.02, 0.98, s=labels[1], size="large", ha="left", va="top")
    axis.text(0.98, 0.02, s=labels[0], size="large", ha="right", va="bottom")


@overload
def scatter_comparison(
    data: np.ndarray,
    opacity: Optional[np.ndarray] = ...,
    labels: Optional[Sequence[str]] = ...,
    axes: None = ...,
    max_cols: int = ...,
    draw_hist: bool = ...,
    color: Optional[tuple[float, float, float]] = ...,
    color_ml: Optional[tuple[float, float, float]] = ...,
    color_dl: Optional[tuple[float, float, float]] = ...,
) -> tuple[Figure, Axes]:
    ...


@overload
def scatter_comparison(
    data: np.ndarray,
    opacity: Optional[np.ndarray] = ...,
    labels: Optional[Sequence[str]] = ...,
    axes: Union[Axes, np.ndarray] = ...,
    max_cols: int = ...,
    draw_hist: bool = ...,
    color: Optional[tuple[float, float, float]] = ...,
    color_ml: Optional[tuple[float, float, float]] = ...,
    color_dl: Optional[tuple[float, float, float]] = ...,
) -> None:
    ...


def scatter_comparison(
    data: np.ndarray,
    opacity: Optional[np.ndarray] = None,
    labels: Optional[Sequence[str]] = None,
    axes: Optional[Union[Axes, np.ndarray]] = None,
    max_cols: int = 4,
    draw_hist: bool = False,
    color: Optional[tuple[float, float, float]] = None,
    color_ml: Optional[tuple[float, float, float]] = None,
    color_dl: Optional[tuple[float, float, float]] = None,
) -> Optional[tuple[Figure, Union[Axes, np.ndarray]]]:
    """Creates scatterplots comparing the data of different categories.
    This produces plots for each combination of rows in the given
    ``data`` array.
    The plots also contain a vertical and horizontal line indicating the
    mean accuracy values of the classifiers. The line corresponding to
    the lower mean is dashed.

    Args:
        data (np.ndarray): A two dimensional array, e.g. consisting of
            accuracy values from different classifiers.
        opacity (np.ndarray, optional): Opacity values that are used to
            set alpha color values to the points in the scatter plot.
            The length of this array has to be the same as the size of
            the second dimension in ``data``.
        labels (Sequence[str], optional): A number of strings matching
            names of the categories or classifiers that are being
            compared. The length of this sequence has to match
            ``data.shape[0]``.
        axes (Axes | np.ndarray, optional): One or multiple axes in
            a numpy array. The plots will be drawn on these axes.
        max_cols (int, optional): If ``axes`` is not specified, this
            integer is the number of columns in a figure to fill before
            starting a new row of scatterplots. Defaults to 4.
        draw_hist (bool, optional): If True, also draws a histogram
            for each category. Defaults to False.
        color (tuple[float, float, float], optional): Color of points in
            the scatterplots.
        color_dl (tuple[float, float, float], optional): Color of the
            diagonal lines.
        color_ml (tuple[float, float, float], optional): Color of the
            lines for the mean values on each axis.

    Returns:
        Pyplot figure and axes containing all plots or None if ``axes``
        is specified.
    """
    fig = None
    if data.ndim != 2:
        raise ValueError("Expected two dimensional data array, "
                         f"got {data.ndim}")
    n_classifiers, n_datasets = data.shape
    if opacity is not None and len(opacity) != n_datasets:
        raise ValueError(f"length of 'opacity' ({len(opacity)}) does not match"
                         f" data shape; should be {n_datasets}")
    if labels is not None and len(labels) != n_classifiers:
        raise ValueError(f"length of 'labels' ({len(labels)}) does not match"
                         f" data shape; should be {n_classifiers}")

    color = color if color is not None else (0.9, 0.5, 0.3)
    labels = labels if labels is not None else (
        [f"{i+1}" for i in range(n_classifiers)]
    )
    if n_classifiers == 1:
        if axes is not None:
            if not isinstance(axes, Axes):
                raise ValueError(f"Expected a single axes, got {type(axes)}")
            return _hist(data, axis=axes, label=labels[0], color=color)
        else:
            fig, axs = plt.subplots(1, 1)
            _hist(data, axis=axs, label=labels[0], color=color)
            return fig, axs

    color_dl = color_dl if color_dl is not None else (0.2, 0.1, 0.7)
    color_ml = color_ml if color_ml is not None else (0.2, 0.4, 0.3)
    if axes is None:
        cols = n_plots = int(n_classifiers * (n_classifiers-1) / 2)
        if draw_hist:
            cols += n_classifiers
            n_plots = cols
        rows = 1
        if n_plots > max_cols:
            cols = max_cols
            rows = n_plots // max_cols
            if n_plots % max_cols != 0:
                rows += 1
        fig, axs = plt.subplots(rows, cols)
        axs = np.array(axs).reshape((rows, cols))
    else:
        if isinstance(axes, Axes):
            if n_classifiers > 2:
                raise ValueError("Expected an array of axes")
            axes = np.array([[axes]])
        axs = axes

    if draw_hist:
        indices = combinations_with_replacement(range(n_classifiers), r=2)
    else:
        indices = combinations(range(n_classifiers), r=2)
    i = j = 0
    for ii, jj in indices:
        if j == axs.shape[1]:
            j = 0
            i += 1
        axs[i, j].axis('square')
        axs[i, j].set_xlim([0, 1])
        axs[i, j].xaxis.set_ticks(
            ticks=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
            labels=["", "", "", "", "", ""],
        )
        axs[i, j].xaxis.set_ticks(
            ticks=[0.1, 0.3, 0.5, 0.7, 0.9],
            labels=["", "", "", "", ""],
            minor=True,
        )
        axs[i, j].yaxis.set_ticks(
            ticks=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
            labels=["", "", "", "", "", ""],
        )
        axs[i, j].yaxis.set_ticks(
            ticks=[0.1, 0.3, 0.5, 0.7, 0.9],
            labels=["", "", "", "", ""],
            minor=True,
        )
        axs[i, j].set_ylim([0, 1])
        axs[i, j].tick_params(which="both", direction="in")
        if ii == jj:
            _hist(
                data[ii],
                axis=axs[i, j],
                label=labels[ii],
                color=color,
            )
        else:
            _scattercomp(
                data[np.array([ii, jj]), :],
                axis=axs[i, j],
                opacity=opacity,
                labels=(labels[ii], labels[jj]),
                color=color,
                color_dl=color_dl,
                color_ml=color_ml,
            )
        j += 1
    while j < axs.shape[1]:
        axs[i, j].axis('off')
        j += 1
    if fig is not None:
        return fig, axs
    return None
