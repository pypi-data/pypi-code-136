import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class NpPdTransformer(BaseEstimator, TransformerMixin):
    def __init__(self) -> None:
        self.columns = []

    def fit(self, X, y=None):
        self.columns = X.columns
        return self

    def transform(self, X, y=None):
        if isinstance(X, pd.DataFrame):
            return X

        return pd.DataFrame(X, columns=self.columns)
