from scipy import stats
from xgboost import XGBRegressor
import numpy as np
import pandas as pd


def verify_ml_dataset(dataset):
    # check for null values in pandas dataframe
    DATA_IMBALANCE_THRESHOLD = 0.1
    TOO_MANY_ZEROES_THRESHOLD = 0.1
    FEATURE_IMPORTANCE_THRESHOLD = 0.01
    dict = {"errors": [], "warnings": [], "success": []}
    Y = pd.DataFrame()

    # check for null values in pandas dataframe
    if dataset.isnull().values.any():
        dict["errors"].append("null_values")
    else:
        dict["success"].append("null_values")

    # check for label config
    for column in dataset.columns:
        if "label" in column:
            Y[column] = dataset[column]
            dataset.drop(column, axis=1, inplace=True)
    if Y.empty:
        dict["errors"].append("label")
    else:
        dict["success"].append("label")

    # check for string columns in pandas dataframe
    if (dataset.dtypes == object).sum() > 0:
        dict["errors"].append("string_features")
    else:
        dict["success"].append("string_features")

    # check for too many zeroes in pandas dataframe
    count = 0
    for column_name in dataset.columns:
        column = dataset[column_name]
        count += (column == 0).sum()
        if count > len(dataset) * TOO_MANY_ZEROES_THRESHOLD:
            dict["warnings"].append("too_many_zeroes")
            break

    # Check for outliers
    if "string_features" in dict["success"]:
        z_scores = stats.zscore(dataset)
        abs_z_scores = np.abs(z_scores)
        # Select data points with a z-scores above or below 3
        filtered_entries = (abs_z_scores < 3).all(axis=1)
        if len(filtered_entries) > 0:
            dict["warnings"].append("outliers")
        else:
            dict["success"].append("outliers")

    # Check for data imbalance
    if "label" in dict["success"]:
        try:
            values = Y.value_counts()
            if (
                values[0] * DATA_IMBALANCE_THRESHOLD > values[1]
                or values[1] * DATA_IMBALANCE_THRESHOLD > values[0]
            ):
                dict["warnings"].append("data_imbalance")
            else:
                dict["success"].append("data_imbalance")
        except:
            labels = []
            for column_name in Y.columns:
                if "label" in column_name:
                    labels.append(dataset[column_name][1])
            labels.sort()
            if (
                labels[0] * DATA_IMBALANCE_THRESHOLD > labels[-1]
                or labels[-1] * DATA_IMBALANCE_THRESHOLD > labels[0]
            ):
                dict["warnings"].append("data_imbalance")
            else:
                dict["success"].append("data_imbalance")
    # check for feature importance
    if "string_features" in dict["success"]:
        xgb = XGBRegressor()
        xgb.fit(dataset, Y)
        importance = xgb.feature_importances_
        for score in importance:
            if score < FEATURE_IMPORTANCE_THRESHOLD:
                dict["warnings"].append("low_importance_features")
                break
        else:
            dict["success"].append("low_importance_features")

    # Data normalization
    if "string_features" in dict["success"]:
        for val in dataset.min():
            if val < -1:
                dict["warnings"].append("data_normalization")
                break
        else:
            dict["success"].append("data_normalization")
        for val in dataset.max():
            if val > 1:
                dict["warnings"].append("data_normalization")
                break
        else:
            dict["success"].append("data_normalization")

    return dict
