import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np


def resize(coverage, dimensions, down=True, up=True):
    def inner(coverage, axis, target):
        size = coverage.shape[axis]
        if not ((size > target and down) or (size < target and up)):
            return coverage
        end = size - 1
        indexes = np.linspace(0, end, target, endpoint=True).round().astype(int)
        return coverage.take(indexes, axis=axis)
    for axis, to in enumerate(dimensions):
        if to is None:
            continue
        coverage = inner(coverage, axis, to)
    return coverage


def infer_background(coverages, random=None):
    if np.isscalar(random):
        return random
    random = []
    for coverage in coverages:
        span = max(min(coverage.shape[1] // 10, 10), 1)
        left_average = coverage[:, :span].mean()
        right_average = coverage[:, -span:].mean()
        average = (left_average + right_average) / 2
        random.append(average)
    clip_range = np.quantile(random, 0.1), np.quantile(random, 0.9)
    clipped = np.clip(random, *clip_range)
    return np.mean(clipped)


def infer_shape(coverages, background):
    differences = []
    for coverage in coverages:
        profile = coverage.mean(axis=0)
        gain = profile.max() - background
        loss = background - profile.min()
        difference = gain - loss
        differences.append(difference)
    score = np.sum(differences)
    return "gain" if score >= 0 else "loss"


def infer_contrast(coverages, background, shape, aggressive=False):
    if len(coverages) > 1:
        contrasts = [
            infer_contrast([coverage], background, shape, aggressive)
            for coverage in coverages]
        min_value = min(contrast[0] for contrast in contrasts)
        max_value = max(contrast[1] for contrast in contrasts)
        return min_value, max_value
    if shape == "symmetrical":
        min_value = infer_contrast(coverages, background, "loss", aggressive)[0]
        max_value = infer_contrast(coverages, background, "gain", aggressive)[1]
        max_difference = max(max_value - background, background - min_value)
        return background - max_difference, background + max_difference
    where = dict(gain=np.argmax, loss=np.argmin)[shape]
    profile = coverages[0].mean(axis=0)
    values = np.sort(coverages[0][:, where(profile)])
    indexes = np.arange(len(values))
    for iteration in range(10):
        slope, intercept = np.polyfit(x=indexes, y=values, deg=1)
        min_value = slope * indexes[0] + intercept
        max_value = slope * indexes[-1] + intercept
        if aggressive:
            values = values[(values >= min_value) & (values <= max_value)]
            indexes = np.arange(len(values))
            if not len(values):
                break
        else:
            np.clip(values, min_value, max_value, out=values)
        if iteration and 0.99 <= slope / previous_slope <= 1.01:
            break
        previous_slope = slope
    min_value = min_value if shape == "loss" else background
    max_value = max_value if shape == "gain" else background
    return min_value, max_value


def get_color(input):
    if not isinstance(input, str):
        return input
    if input.startswith("#"):
        return matplotlib.colors.to_rgb(input)
    available = {
        "white": "#ffffff", "black": "#000000", "slate": "#64748b",
        "gray": "#6b7280", "zinc": "#71717a", "neutral": "#737373",
        "stone": "#78716c", "red": "#ef4444", "orange": "#f97316",
        "amber": "#f59e0b", "yellow": "#eab308", "lime": "#84cc16",
        "green": "#22c55e", "emerald": "#10b981", "teal": "#14b8a6",
        "cyan": "#06b6d4", "sky": "#0ea5e9", "blue": "#3b82f6",
        "indigo": "#6366f1", "violet": "#8b5cf6", "purple": "#a855f7",
        "fuchsia": "#d946ef", "pink": "#ec4899", "rose": "#f43f5e"}
    return get_color(available[input.strip().lower()])


def get_color_map(input):
    if isinstance(input, matplotlib.colors.Colormap):
        return input
    if isinstance(input, str):
        input = input.lower()
        available = {name.lower(): name for name in plt.colormaps()}
        if input in available:
            return matplotlib.colors.Colormap(available[input])
        input = input.split(",") if "," in input else ["white", input]
    input = [get_color(entry) for entry in input]
    LinearSegmentedColormap = matplotlib.colors.LinearSegmentedColormap
    return LinearSegmentedColormap.from_list("cmap", input)


def intialize(
    array,
    list_names,
    target_names,
    sample=None,
    backgrounds=None,
    randoms=None,
    shapes=None,
    default_shape="symmetrical",
    contrasts=None,
    aggressive_contrast=False,
    gradients=None,
    default_gradient="black",
    default_symmetrical_gradient="sky,white,rose"):

    sample = sample or [None, None]
    list_count = len(list_names)
    target_count = len(target_names)
    settings = {
        "lists": {"count": list_count, "names": list_names},
        "targets": {
            "count": target_count,
            "names": target_names,
            "backgrounds": [],
            "shapes": [],
            "contrasts": [],
            "gradients": []},
        "entries": []}
    for list_index in range(list_count):
        settings["entries"].append([])
        for target_index in range(target_count):
            values = array[list_index][target_index]
            values = resize(values, sample, up=False)
            settings["entries"][-1].append(values)
    for target_index in range(target_count):
        values = [row[target_index] for row in settings["entries"]]
        background = backgrounds[target_index] if backgrounds else None
        random = randoms[target_index] if randoms else None
        shape = shapes[target_index] if shapes else None
        contrast = contrasts[target_index] if contrasts else None
        gradient = gradients[target_index] if gradients else None
        if background is None:
            background = infer_background(values, random)
        if shape is None:
            shape = \
                infer_shape(values, background) \
                if default_shape is None \
                else default_shape
        if contrast is None:
            contrast = infer_contrast(values, background, shape, aggressive_contrast)
        if gradient is None:
            gradient = \
                default_symmetrical_gradient \
                if shape == "symmetrical" \
                else default_gradient
        settings["targets"]["backgrounds"].append(background)
        settings["targets"]["shapes"].append(shape)
        settings["targets"]["contrasts"].append(contrast)
        settings["targets"]["gradients"].append(gradient)
    return settings


def plot(settings, entry_size=(3, 6)):
    total_vertical_count = sum(row[0].shape[0] for row in settings["entries"])
    height_ratios = [row[0].shape[0] / total_vertical_count for row in settings["entries"]]
    fig, axs = plt.subplots(
        settings["lists"]["count"],
        settings["targets"]["count"],
        figsize=(
            entry_size[0] * settings["targets"]["count"],
            entry_size[1] * settings["lists"]["count"]),
        gridspec_kw={"height_ratios": height_ratios},
        sharex="col",
        sharey="row",
        squeeze=False)
    for target_index in range(settings["targets"]["count"]):
        contrast = settings["targets"]["contrasts"][target_index]
        color_map = get_color_map(settings["targets"]["gradients"][target_index])
        for list_index in range(settings["lists"]["count"]):
            values = settings["entries"][list_index][target_index]
            ax = axs[list_index, target_index]
            ax.imshow(
                values,
                cmap=color_map,
                vmin=contrast[0],
                vmax=contrast[1],
                interpolation="nearest")
    for ax, name in zip(axs[:, 0], settings["lists"]["names"]):
        ax.set_ylabel(name, size="large")
    for ax, name in zip(axs[0], settings["targets"]["names"]):
        ax.set_title(name)
    fig.tight_layout()
    return fig


def plot_individually(settings, entry_size=(3, 6):
    total_vertical_count = sum(row[0].shape[0] for row in settings["entries"])
    height_ratios = [row[0].shape[0] / total_vertical_count for row in settings["entries"]]
    for target_index in range(settings["targets"]["count"]):
        contrast = settings["targets"]["contrasts"][target_index]
        color_map = get_color_map(settings["targets"]["gradients"][target_index])
        color_map = (np.array([color_map(x) for x in range(255)]) * 255).round().astype(np.uint8)
        for list_index in range(settings["lists"]["count"]):
            height = entry_size[1] * 100 * height_ratios[list_index]
            width = entry_size[0] * 100
            values = settings["entries"][list_index][target_index]
            values = resize(values, [height, width])






