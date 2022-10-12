import abc
import os
from abc import ABC
from pathlib import Path
from typing import List, Union

import numpy as np
import pandas as pd
import requests
from sklearn.model_selection import train_test_split

from mlc.constraints.constraints import (
    BaseRelationConstraint,
    get_constraints_from_metadata,
)


class DataSource(ABC):
    @abc.abstractmethod
    def load_data(self):
        pass


class FileDataSource(DataSource, ABC):
    def __init__(self, path: str):
        self.path = path

    def get_path(self):
        return self.path


class CsvDataSource(FileDataSource):
    def __init__(self, path: str, **kwargs):
        self.pandas_params = kwargs
        super(CsvDataSource, self).__init__(path)

    def load_data(self):
        return pd.read_csv(self.path, **self.pandas_params, low_memory=False)


class DownloadFileDataSource(DataSource):
    def __init__(
        self, url: str, file_data_source: FileDataSource, overwrite=False
    ):
        self.url = url
        self.file_data_source = file_data_source
        self.overwrite = overwrite

    def load_data(self):
        path = self.file_data_source.get_path()
        if self.overwrite or (not os.path.exists(path)):
            Path(path).parent.mkdir(parents=True, exist_ok=True)
            data = requests.get(self.url)
            with open(path, "wb") as file:
                file.write(data.content)
        return self.file_data_source.load_data()


class TaskProcessor(ABC):
    @abc.abstractmethod
    def transform(self, task_data):
        pass


class Task:
    def __init__(
        self,
        name: Union[int, str],
        task_type: str,
        evaluation_metric: str,
        task_processor: TaskProcessor = None,
    ):
        self.name = name
        self.type = task_type
        self.evaluation_metric = evaluation_metric
        self.task_processor = task_processor


class Sorter(ABC):
    @abc.abstractmethod
    def get_index(self, data) -> Union[pd.Series, np.ndarray]:
        pass


class DefaultIndexSorter(Sorter):
    def get_index(self, data) -> Union[pd.Series, np.ndarray]:
        return np.arange(len(data))


class DateSorter(Sorter):
    def __init__(self, date_col: str):
        self.date_col = date_col

    def get_index(self, data) -> Union[pd.Series, np.ndarray]:
        return pd.to_datetime(data[self.date_col])


class Splitter(ABC):
    @abc.abstractmethod
    def get_splits(self, dataset):
        pass


class DefaultSplitter(Splitter):
    def __init__(self, test_size=0.2, random_seed=42):
        self.test_size = test_size
        self.random_seed = random_seed

    def get_splits(self, dataset):
        _, y = dataset.get_x_y()
        i = np.arange(len(y))
        i_train, i_test = train_test_split(
            i,
            random_state=self.random_seed,
            shuffle=True,
            stratify=y[i],
            test_size=self.test_size,
        )
        i_train, i_val = train_test_split(
            i_train,
            random_state=self.random_seed,
            shuffle=True,
            stratify=y[i_train],
            test_size=self.test_size,
        )
        return {"train": i_train, "val": i_val, "test": i_test}


class Dataset:
    def __init__(
        self,
        name: str,
        data_source: DataSource,
        metadata_source: DataSource,
        tasks: List[Task],
        sorter: Sorter,
        splitter: Union[Splitter, None],
        relation_constraints: List[BaseRelationConstraint] = None,
    ):

        self.name = name
        self.data_source = data_source
        self.metadata_source = metadata_source
        self.splitter = splitter
        self.tasks = tasks
        self.sorter = sorter
        self.relation_constraints = relation_constraints

        self.data = None
        self.metadata = None

    def get_name(self):
        return self.name

    def get_data(self):
        if self.data is None:
            self.data = self.data_source.load_data()
        return self.data.copy()

    def get_metadata(self, only_x=False):
        if self.metadata is None:
            self.metadata = self.metadata_source.load_data()
        metadata = self.metadata.copy()
        if only_x:
            x_col = self.get_x_y()[0].columns
            metadata = metadata[metadata["feature"].isin(x_col)]

        return metadata

    def get_x_y(self, keep_date=False):
        data = self.get_data()
        y = []
        for task in self.tasks:
            task_data = data[task.name]
            if task.task_processor is not None:
                task_data = task.task_processor.transform(task_data)
            data = data.drop(columns=task.name)
            y.append(task_data)

        y = np.array(y)
        if y.shape[0] == 1:
            y = y.ravel()

        if isinstance(self.sorter, DateSorter) and (not keep_date):
            data = data.drop(columns=self.sorter.date_col)

        return data, y

    def get_x_y_t(self, keep_date=False):
        x, y = self.get_x_y(keep_date=True)
        t = self.sorter.get_index(x)
        if isinstance(self.sorter, DateSorter) and (not keep_date):
            x = x.drop(columns=self.sorter.date_col)
        return x, y, t

    def get_splits(self):
        return self.splitter.get_splits(self)

    def get_constraints(self):
        metadata = self.get_metadata()
        col_filter = self.get_x_y()[0].columns.to_list()
        return get_constraints_from_metadata(
            metadata, self.relation_constraints, col_filter
        )
