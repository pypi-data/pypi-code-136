from mlc.datasets.dataset import (
    CsvDataSource,
    Dataset,
    DateSorter,
    DefaultSplitter,
    Task,
    TaskProcessor,
)


class RegressionClassificationProcessor(TaskProcessor):
    def transform(self, task_data):
        return (task_data > 0).astype(int)


data_source = CsvDataSource(path="./data/mlc/airlines/flight_delay_ord.csv")
metadata_source = CsvDataSource(
    path="./data/mlc/airlines/flight_delay_ord_metadata.csv"
)
sorter = DateSorter(date_col="date_time")
splitter = DefaultSplitter()

flight_delay_ord_regression_dataset = Dataset(
    name="flight_delay_ord_regress",
    data_source=data_source,
    metadata_source=metadata_source,
    tasks=[
        Task(
            name="ArrDelay",
            task_type="classification",
            evaluation_metric="f1_score",
        )
    ],
    sorter=sorter,
    splitter=splitter,
    relation_constraints=[],
)

flight_delay_ord_classification_dataset = Dataset(
    name="flight_delay_ord_class",
    data_source=data_source,
    metadata_source=metadata_source,
    tasks=[
        Task(
            name="ArrDelay",
            task_type="classification",
            evaluation_metric="f1_score",
            task_processor=RegressionClassificationProcessor(),
        )
    ],
    sorter=sorter,
    splitter=splitter,
    relation_constraints=[],
)

datasets = [
    flight_delay_ord_regression_dataset,
    flight_delay_ord_classification_dataset,
]
