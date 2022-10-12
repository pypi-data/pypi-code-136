from mlc.datasets.dataset import (
    CsvDataSource,
    Dataset,
    DateSorter,
    DefaultSplitter,
    Task,
)

electricity_dataset = Dataset(
    name="electricity",
    data_source=CsvDataSource(path="./data/mlc/electicity/electricity.csv"),
    metadata_source=CsvDataSource(
        path="./data/mlc/electicity/electricity_metadata.csv"
    ),
    tasks=[
        Task(
            name="price_up",
            task_type="classification",
            evaluation_metric="f1_score",
        )
    ],
    sorter=DateSorter(date_col="date_time"),
    splitter=DefaultSplitter(),
    relation_constraints=[],
)

datasets = [electricity_dataset]
