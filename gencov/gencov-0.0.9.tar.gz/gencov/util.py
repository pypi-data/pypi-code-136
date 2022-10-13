import argparse
import gzip
import importlib
import os
import struct
import sys


class ArgumentParser(argparse.ArgumentParser):

    def error(self, message):
        message = f"failed to parse command line: {message}"
        raise RuntimeError(message)


class gz_open:

    def __init__(self, path, mode="r", gz=None, gz_level=6):
        self.path = path
        self.mode = mode if "b" in mode or "t" in mode else f"{mode[:1]}t{mode[1:]}"
        self.gz = self.is_gz(path) if gz is None else gz
        self.gz_level = gz_level

    def __enter__(self):
        if self.gz:
            self.file = gzip.open(self.path, self.mode, self.gz_level)
        else:
            self.file = open(self.path, self.mode)
        return self.file
        
    def __exit__(self, exc_type, exc_value, exc_trace):
        self.file.close()

    @classmethod
    def is_gz(cls, path, use="magic"):
        if use == "magic":
            with open(path, "rb") as file:
                return file.read(2) == b"\x1f\x8b"
        elif use == "extension":
            return path.lower().endswith(".gz")
        raise ValueError(f"use magic or extension, not {use}")

    @classmethod
    def get_format(cls, path):
        base, extension = os.path.splitext(path)
        if extension.lower() == ".gz":
            base, extension = os.path.splitext(base)
        return extension


class shut_up:

    def __init__(self, streams=("stdout", "stderr")):
        self.streams = []
        for stream in streams:
            if isinstance(stream, str):
                stream = getattr(sys, stream)
            stream = dict(f=stream)
            stream["fd"] = stream["f"].fileno()
            stream["dup_fd"] = os.dup(stream["fd"])
            stream["tmp_f"] = open(os.devnull, "w")
            stream["tmp_fd"] = stream["tmp_f"].fileno()
            os.dup2(stream["tmp_fd"], stream["fd"])
            self.streams.append(stream)
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_trace):
        self.close()

    def close(self):
        for stream in self.streams:
            os.dup2(stream["dup_fd"], stream["fd"])
            stream["tmp_f"].close()


def merge_intervals(intervals, already_sorted=False):
    if not already_sorted:
        intervals = sorted(intervals, key=lambda interval: interval[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged


def arr_to_bin(arr):
    n_windows = len(arr)
    n_bins = len(arr[0])
    bin_data = [struct.pack("<2Q", n_windows, n_bins)]
    win_struct = struct.Struct(f"<{n_bins}f")
    for window in arr:
        bin_data.append(win_struct.pack(*window))
    return b"".join(bin_data)
 
 
def bin_to_arr(bin_data):
    n_windows, n_bins = struct.unpack("<2Q", bin_data[:16])
    win_struct = struct.Struct(f"<{n_bins}f")
    arr = []
    for i_window in range(n_windows):
        i = 16 + i_window * 4 * n_bins
        j = i + 4 * n_bins
        arr.append(list(win_struct.unpack(bin_data[i:j])))
    return arr


def linspace(start, stop, count, endpoint=True):
    if endpoint:
        if count == 1:
            return start
        step = (stop - start) / (count - 1)
    else:
        step = (stop - start) / count
    return [start + step * i for i in range(count)]


class LazyImport:

    def __init__(self, name, package=None, path=None):
        """
        lazy import module (imported at first attribute accession)

        arguments:
            name: module name
            package: module anchor to resolve relative import
            path: module location (package argument ignored)
        """
        self.name = name
        self.package = package
        self.path = path
        self.module = None

    def __repr__(self):
        name = object.__getattribute__(self, "name")
        if object.__getattribute__(self, "module"):
            return f"<module {name!r} lazy imported>"
        return f"<module {name!r} not yet imported>"

    def __getattribute__(self, key):
        module = object.__getattribute__(self, "module")
        if not module:
            name = object.__getattribute__(self, "name")
            package = object.__getattribute__(self, "package")
            path = object.__getattribute__(self, "path")
            load = object.__getattribute__(self, "load")
            module = load(name, package, path)
            self.module = module
        return getattr(module, key)
    
    @staticmethod
    def load(name, package=None, path=None):
        if path:
            spec = importlib.util.spec_from_file_location(name, path)
            module = importlib.util.module_from_spec(spec)
            sys.modules[name] = module
            spec.loader.exec_module(module)
        else:
            module = importlib.import_module(name, package)
        return module
