import pandas as pd


def parse_dataset(dataset):
    dict = {}
    dict["rows"] = len(dataset)
    dict["columns"] = []
    for column in dataset.columns:
        if (
            column.lower() == "location"
            or column.lower() == "city"
            or column.lower() == "country"
            or column.lower() == "state"
        ):
            dict["columns"].append({"name": column, "type": "location"})
        if (
            column
            in dataset.select_dtypes(
                include=["int64", "float64", "int32", "float32"]
            ).columns.values
        ):
            dict["columns"].append({"name": column, "type": "numeric"})
        elif column in dataset.select_dtypes(include=["object"]).columns.values:
            if len(dataset[column].unique()) < len(dataset) * 0.1:
                dict["columns"].append({"name": column, "type": "categorical"})
                continue
            try:
                pd.to_datetime(dataset[column], dayfirst=True)
                dict["columns"].append({"name": column, "type": "datetime"})
                continue
            except:
                dict["columns"].append({"name": column, "type": "text"})
    return dict
