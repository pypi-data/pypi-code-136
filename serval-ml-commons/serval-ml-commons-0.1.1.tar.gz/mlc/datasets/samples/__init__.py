from typing import List, Union

from mlc.datasets.dataset import Dataset
from mlc.datasets.samples.airlines import datasets as airlines_datasets
from mlc.datasets.samples.ctu_13_neris import datasets as ctu_13_neris_datasets
from mlc.datasets.samples.electricity import datasets as electricity_datasets
from mlc.datasets.samples.lcld import datasets as lcld_datasets
from mlc.datasets.samples.url import datasets as url_datasets

datasets: List[Dataset] = (
    lcld_datasets
    + ctu_13_neris_datasets
    + electricity_datasets
    + airlines_datasets
    + url_datasets
)


def load_dataset(dataset_name: str) -> Dataset:
    return load_datasets(dataset_name)[0]


def load_datasets(dataset_names: Union[str, List[str]]) -> List[Dataset]:

    if isinstance(dataset_names, str):
        dataset_names = [dataset_names]
    datasets_out = list(filter(lambda e: e.name in dataset_names, datasets))

    if len(datasets_out) != len(dataset_names):
        raise NotImplementedError("At least one dataset is not available.")

    return datasets_out
