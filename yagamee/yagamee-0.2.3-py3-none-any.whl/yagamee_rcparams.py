from matplotlib import cycler

figure_defaults = {
    "figure.figsize": [9.0, 4.8],
    "figure.facecolor": "white",
}
tick_defaults = {
    "xtick.direction": "in",
    "ytick.direction": "in",
}
yagamee_rcparams = dict({}, **figure_defaults, **tick_defaults)