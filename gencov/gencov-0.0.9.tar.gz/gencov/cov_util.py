import math
import statistics

from .io import BigwigReader, read_loci_signal


def parse_window_setting(setting):
    try:
        center, left, right = setting.split("/")
        left, right = int(left), int(right)
        if left >= right: raise Exception()
    except Exception:
        message = f"{setting} as center/left/right with left < right"
        raise ValueError(f"invalid window: {message}")
    return center, left, right


def get_windows_bounds(centers, left, right, strands=None):
    bounds = []
    if strands is None:
        for center in centers:
            start = center + left
            end = center + right
            bounds.append((start, end))
    else:
        for center, strand in zip(centers, strands):
            if strand == "+":
                start = center + left
                end = center + right
            elif strand == "-":
                start = center - right
                end = center - left
            else:
                raise ValueError(f"invalid strand: {strand} (+, -)")
            bounds.append((start, end))
    return list(zip(*bounds))


def get_window_scale(left, right, bin_size, col_count=None):
    scale = list(range(left, right, bin_size))
    if col_count is not None:
        initial_col_count = len(scale)
        indexes = [
            int(round(index * (initial_col_count - 1) / (col_count - 1)))
            for index in range(col_count)]
        scale = [scale[index] for index in indexes]
    return scale


def get_coverage_at_loci(path, chr_ids, starts, ends, bin_size, default_value=None, strands=None):
    return read_loci_signal(path, chr_ids, starts, ends, strands=strands, bin_size=bin_size, default_value=default_value)


def parse_sample_setting(setting, row_count=None, col_count=None):
    try:
        if row_count is not None:
            setting = f"{row_count}/{setting}"
        if col_count is not None:
            if "/" in setting:
                setting = f"{setting[:setting.index('/')]}" \
                    f"/{col_count}{setting[setting.index('/'):]}"
            else:
                setting = f"{setting}/{col_count}"
        parts = setting.split("/")
        if len(parts) == 2: parts.append("nearest")
        row_count, col_count, method = parts
        row_count = None if row_count == "all" else int(row_count)
        col_count = None if col_count == "all" else int(col_count)
        if method not in ["nearest", "area"]: raise Exception()
    except Exception:
        message = f"{setting} as row_count/column_count(/method) " \
            "with row_count and column_count as all, integer " \
            "and method as nearest, area"
        raise ValueError(f"invalid sample: {message}")
    return row_count, col_count, method


def sample_coverage(values, row_count=None, col_count=None, method="nearest"):
    if not values:
        return values
    initial_row_count = len(values)
    if row_count is None:
        row_count = initial_row_count
    initial_col_count = len(values[0])
    if col_count is None:
        col_count = initial_col_count
    if method not in ["nearest", "area"]:
        raise ValueError(f"invalid sample method: {method} (nearest, area)")
    if row_count < initial_row_count:
        if method == "nearest":
            indexes = [
                int(round(index * (initial_row_count - 1) / (row_count - 1)))
                for index in range(row_count)]
            values = [values[index] for index in indexes]
        else:
            factor = initial_row_count / row_count
            indexes = list(range(initial_row_count))
            indexes = [
                indexes[int(round(index * factor)):int(round((index + 1) * factor))]
                for index in range(row_count)]
            values = [[
                    sum(values[index][col_index] for index in bin_indexes) / len(bin_indexes)
                    for col_index in range(initial_col_count)]
                for bin_indexes in indexes]
    elif row_count > initial_row_count:
        indexes = [
            int(round(index * (initial_row_count - 1) / (row_count - 1)))
            for index in range(row_count)]
        values = [values[index] for index in indexes]
    if col_count < initial_col_count:
        if method == "nearest":
            indexes = [
                int(round(index * (initial_col_count - 1) / (col_count - 1)))
                for index in range(col_count)]
            values = [[row[index] for index in indexes] for row in values]
        else:
            factor = initial_col_count / col_count
            indexes = list(range(initial_col_count))
            indexes = [
                indexes[int(round(index * factor)):int(round((index + 1) * factor))]
                for index in range(col_count)]
            values = [[
                    sum(values[row_index][index] for index in bin_indexes) / len(bin_indexes)
                    for bin_indexes in indexes]
                for row_index in range(row_count)]
    elif col_count > initial_col_count:
        indexes = [
            int(round(index * (initial_col_count - 1) / (col_count - 1)))
            for index in range(col_count)]
        values = [[row[index] for index in indexes] for row in values]
    return values
            

def parse_average_setting(setting):
    try:
        parts = setting.split(":")
        method = parts[0]
        if method in ["mean", "sd", "sem", "median", "l1norm", "l2norm"]:
            if parts[1:]: raise Exception()
            args = []
        elif method == "quantile":
            quantile, = parts[1:]
            args = [float(quantile)]
        else:
            raise Exception()
    except Exception:
        message = f"{setting} as method " \
            "with method as mean, sd, sem, median, quantile:number, l1norm, l2norm"
        raise ValueError(f"invalid average: {message}")
    return method, args


def average_coverage(values, by, method, *args):
    if by == "rows":
        values = list(map(list, zip(*values)))
    elif by not in ["cols", "columns"]:
        raise ValueError(f"invalid average by: {by} (rows, columns)")
    if method == "mean":
        result = [statistics.mean(row) for row in values]
    elif method == "sd":
        result = [statistics.stddev(row) for row in values]
    elif method == "sem":
        sds = [statistics.stddev(row) for row in values]
        result = [sd / math.sqrt(len(row)) for sd, row in zip(sds, values)]
    elif method == "median":
        result = [statistics.median(row) for row in values]
    elif method == "quantile":
        import numpy as np
        result = np.quantile(values, args[0], axis=1).tolist()
    elif method == "l1norm":
        result = [sum(abs(value) for value in row) for row in values]
    elif method == "l2norm":
        result = [math.sqrt(sum(value ** 2 for value in row)) for row in values]
    else:
        raise ValueError(f"invalid average method: {method}")
    return result


def get_bigwig_chr_sizes(path, write_to=None):
    chr_sizes = BigwigReader(path).chr_sizes
    if write_to is not None:
        with open(write_to, "w") as file:
            for chr_id, chr_size in chr_sizes.items():
                file.write(f"{chr_id}\t{chr_size}\n")
    return chr_sizes


def iter_bigwig(path):
    return BigwigReader(path).iter_entries()
