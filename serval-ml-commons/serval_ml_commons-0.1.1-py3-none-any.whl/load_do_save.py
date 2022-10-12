import json
import os.path
from pathlib import Path

import h5py
import joblib
import numpy as np
from sklearn.base import BaseEstimator

cache = []
hdf5_dataset_key = "default"


def load_json(path):
    with open(path, "r") as f:
        obj = json.load(f)
    return obj


def save_json(obj, path):
    with open(path, "w") as f:
        json.dump(obj, f, indent=4)


def load_hdf5(path):

    with h5py.File(path, "r") as f:
        return f[hdf5_dataset_key][()]


def save_hdf5(obj, path):
    with h5py.File(path, "w") as f:
        f.create_dataset(hdf5_dataset_key, data=obj, compression="gzip")


type_to_fun_mapper = [
    {
        "type": np.ndarray,
        "load": load_hdf5,
        "save": save_hdf5,
    },
    {"type": BaseEstimator, "load": joblib.load, "save": joblib.dump},
    {"type": dict, "load": load_json, "save": save_json},
]


def find_mapper(out_type):
    for mapper in type_to_fun_mapper:
        mapper_type = mapper.get("type")
        if issubclass(out_type, mapper_type):
            return mapper


def load_do_save(
    path: str, executable, return_type=None, verbose=False, **kwargs
):
    if return_type is None:
        return_type = executable.__annotations__["return"]

    mapper = find_mapper(return_type)
    if os.path.exists(path):
        load = mapper.get("load")
        out = load(path)
        if verbose:
            print(f"{path} loaded.")
        return out
    else:
        save = mapper.get("save")
        obj = executable(**kwargs)
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        save(obj, path)
        if verbose:
            print(f"{path} saved.")
        return obj
