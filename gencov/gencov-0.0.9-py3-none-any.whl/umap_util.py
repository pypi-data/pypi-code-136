import numpy as np
import pandas as pd
import sklearn.preprocessing
import umap


def make_embedding(data, random_state=0):
    # data: samples * features
    reducer = umap.UMAP(random_state=random_state)
    embedding = reducer.fit_transform(data)
    return embedding


def standardize_data(data):
    scaler = sklearn.preprocessing.StandardScaler()
    result = scaler.fit_transform(data)
    return result


def load_data(path, file_format="tsv"):
    
    if file_format == "tsv":
        return pd.read_csv(path, sep="\t")
    elif file_format == "tsv":
        return pd.read_csv(path, sep="\t")

    




data = [
    [1, 1, 1, 1],
    [1, 2, 1, 1],
    [2, 2, 2, 2],
    [1, 1, 1, 1],
    [1, 2, 1, 1],
    [2, 2, 2, 2],
]

data = standardize_data(data)

embedding = make_embedding(data, random_state=0)
print(embedding)


