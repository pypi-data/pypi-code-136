import importlib
from typing import Union

from mlc.datasets.samples import load_dataset


def get_dataset_from_config(config: dict):
    name = config.get("name")

    # If it is a known dataset
    if len(config.keys()) == 1:
        return load_dataset(name)

    # Else load and do
    models = importlib.import_module(config.get("source")).models
    models_out = list(filter(lambda e: e[0] in [name], models))
    models_out = [e[1] for e in models_out]

    if len(models_out) != 1:
        raise NotImplementedError("At least one model is not available.")
    return models_out[0]


def get_dataset(config: Union[dict, str]):
    if isinstance(config, str):
        config = {"name": config}
    return get_dataset_from_config(config)
