from pathlib import Path
from typing import Union

from mlc.datasets.dataset import (
    CsvDataSource,
    Dataset,
    DateSorter,
    DownloadFileDataSource,
    FileDataSource,
    Task,
)
from mlc.datasets.samples import load_dataset


def get_tasks(config):
    return [Task(**e) for e in config]


def get_sorter(config: dict):
    if "date" in config.keys():
        return DateSorter(config.get("date"))
    else:
        return None


extension_to_file_loader = {".csv": CsvDataSource}


def get_filedatasource(path) -> FileDataSource:
    ext = Path(path).suffix
    if ext not in extension_to_file_loader:
        raise NotImplementedError
    return extension_to_file_loader[ext](path)


def get_datasource(config):
    if "download" in config.keys():
        download = config.get("download")

        return DownloadFileDataSource(
            url=download.get("url"),
            file_data_source=get_filedatasource(download.get("cache")),
        )
    if "file" in config.keys():
        file = config.get("file")
        return get_filedatasource(file.get("path"))


def get_dataset(config: Union[dict, str]):
    if isinstance(config, str):
        config = {"name": config}
    return get_dataset_from_config(config)


def get_dataset_from_config(config: dict):

    name = config.get("name")

    # If it is a known dataset
    if len(config.keys()) == 1:
        return load_dataset(name)

    data_source = get_datasource(config.get("data").get("source"))
    metadata_source = get_datasource(config.get("metadata").get("source"))
    tasks = get_tasks(config.get("tasks"))
    sorter = get_sorter(config.get("sorter"))
    splitter = None
    relation_constraints = []
    return Dataset(
        name=name,
        data_source=data_source,
        metadata_source=metadata_source,
        tasks=tasks,
        sorter=sorter,
        splitter=splitter,
        relation_constraints=relation_constraints,
    )
