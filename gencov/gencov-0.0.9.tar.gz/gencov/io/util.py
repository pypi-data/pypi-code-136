import bz2
import csv
import gzip
import hashlib
import importlib
import lzma
import os
import pickle
import random
import sys


def z_open(path, mode="r", compression="infer", infer_mode="auto", level=6, **open_kargs):
    mode = mode if "b" in mode or "t" in mode else f"{mode[:1]}t{mode[1:]}"
    if compression == "infer":
        compression = infer_compression(path, infer_mode)
    if compression in ("gzip", "gz"):
        return gzip.open(path, mode, level, **open_kargs)
    if compression in ("bzip2", "bz2"):
        return bz2.open(path, mode, level, **open_kargs)
    if compression in ("lzma", "xz"):
        try:
            return lzma.open(path, mode, preset=level, **open_kargs)
        except ValueError as error:
            if "Cannot specify a preset" in str(error):
                return lzma.open(path, mode, **open_kargs)
            raise error
    if compression in (None, ""):
        return open(path, mode, **open_kargs)
    raise ValueError(f"invalid compression: {compression} (gz, bz2, xz, none)")


def infer_compression(path, mode="auto"):
    if mode == "extension":
        extension = os.path.splitext(path)[1].lstrip(".")
        if extension in ("gz", "bz2", "xz"):
            return extension
        return None
    if mode == "magic":
        with open(path, "rb") as file:
            magic = file.read(6)
        if magic[:2] == b"\x1f\x8b":
            return "gz"
        if magic[:3] == b"BZh":
            return "bz2"
        if magic == b"\xfd\x37\x7a\x58\x5a\x00":
            return "xz"
    if mode == "auto":
        mode = "magic" if os.path.isfile(path) else "extension"
        return infer_compression(path, mode)
    raise ValueError(f"invalid infer mode: {mode} (auto, magic or extension)")


class shut_up:

    def __init__(self):
        self.streams = [
            {"f": getattr(sys, target)}
            for target in ("stdout", "stderr")]
            
    def __enter__(self):
        for stream in self.streams:
            stream["fd"] = stream["f"].fileno()
            stream["dup_fd"] = os.dup(stream["fd"])
            stream["tmp_f"] = open(os.devnull, "w")
            stream["tmp_fd"] = stream["tmp_f"].fileno()
            os.dup2(stream["tmp_fd"], stream["fd"])
        return self
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        for stream in self.streams:
            os.dup2(stream["dup_fd"], stream["fd"])
            stream["tmp_f"].close()


class DiskCache:

    def __init__(self, dir_path, name, data=None, compression=6, require_dir=True):
        self.dir_path = dir_path
        self.name = name
        self.compression = compression
        if data:
            self.name = f"{name}.{self.serialize_and_hash(data)}"
        if require_dir and not os.path.isdir(self.dir_path):
            raise FileNotFoundError(f"cache directory {dir_path} not found")
            
    @classmethod
    def serialize_and_hash(cls, data):
        serialized = pickle.dumps(data)
        return hashlib.md5(serialized).hexdigest()

    def get_path(self, data):
        base_path = os.path.join(self.dir_path, self.name)
        data_hash = self.serialize_and_hash(data)
        return f"{base_path}.{data_hash}.pickle.gz"

    def exists(self, path):
        return os.path.isfile(path)
    
    def read(self, path):
        with gzip.open(path, "rb") as file:
            return pickle.load(file)

    def write(self, path, data):
        with gzip.open(path, "wb", self.compression) as file:
            pickle.dump(data, file)
    
    def purge(self, full=False):
        for name in os.listdir(self.dir_path):
            if full or name.startswith(self.name):
                os.remove(os.path.join(self.dir_path, name))


def get_sorting_indices(values):
    return sorted(range(len(values)), key=lambda index: values[index])


def sorted_by_indices(values, sorting_indices):
    return [values[index] for index in sorting_indices]


def linspace(start, stop, count, endpoint=True, integral=False):
    if endpoint:
        if count == 1:
            return start
        step = (stop - start) / (count - 1)
    else:
        step = (stop - start) / count
    if integral:
        return [int(start + step * i) for i in range(count)]
    return [start + step * i for i in range(count)]


def sample(data, target, seed=None, increase=True, order=True):
    generator = random.Random(seed)
    if increase and target > len(data):
        indexes = linspace(0, len(data), target, endpoint=False, integral=True)
        indexes = generator.sample(indexes, target)
    else:
        indexes = generator.sample(range(len(data)), min(target, len(data)))
    indexes = sorted(indexes) if order else indexes
    return [data[index] for index in sorted(indexes)]


def read_csv(path, sep=",", with_header=True, subsample=None, seed=None, types=None, to=None):
    with z_open(path, "r", newline="") as file:
        reader = csv.reader(file, delimiter=sep)
        data = list(reader)
    header = data.pop(0) if with_header else []
    if subsample is not None:
        data = sample(data, subsample, seed=seed, increase=False, order=True)
    for target, convert in (types or {}).items():
        if isinstance(target, str):
            target = header.index(target)
        if isinstance(target, int):
            for row in data:
                row[target] = convert(row[target])
            continue
        raise TypeError("type conversion target must be an int or a str")
    if to is not None:
        data = data_with_header_to_dict(data, header, format=to)
    return (data, header) if with_header else data


def write_csv(path, data, sep=",", header=None):
    with z_open(path, "w", newline="") as file:
        writer = csv.writer(file, delimiter=sep)
        if header is not None:
            writer.writerow(header)
        writer.writerows(data)


def data_with_header_to_dict(data, header, format="columns"):
    if format == "columns":
        return {
            key: [row[index] for row in data]
            for index, key in enumerate(header)}
    if format == "rows":
        return [
            {key: value for key, value in zip(header, row)}
            for row in data]
    raise ValueError(f"invalid format: {format} (columns, rows")


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
