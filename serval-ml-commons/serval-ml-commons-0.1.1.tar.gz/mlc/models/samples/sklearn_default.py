import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor as SKRandomForestRegressor
from sklearn.pipeline import Pipeline

from mlc.datasets.processing import get_numeric_categorical_preprocessor
from mlc.models.model import Model


class RandomForest(Model):
    def __init__(self, x_metadata, name="rf", **kwargs):
        self.x_metadata = x_metadata
        self.rf_args = kwargs
        cat_features = self.x_metadata["type"] == "cat"
        num_features = ~cat_features
        self.model = Pipeline(
            steps=[
                (
                    "pre_process",
                    get_numeric_categorical_preprocessor(
                        numeric_features=self.x_metadata[num_features][
                            "feature"
                        ],
                        categorical_features=self.x_metadata[cat_features][
                            "feature"
                        ],
                    ),
                ),
                ("model", RandomForestClassifier(**self.rf_args)),
            ]
        )
        super(RandomForest, self).__init__(name)

    def fit(self, x, y):
        self.model.fit(x, y)

    def predict(self, x):
        return self.model.predict_proba(x)

    def load(self, path):
        self.model = joblib.load(path)

    def save(self, path):
        joblib.dump(self.model, path)


class RandomForestBalanced(Model):
    def __init__(self, x_metadata, **kwargs):
        name = "rf_balanced"
        self.model = RandomForest(
            x_metadata=x_metadata, class_weight="balanced", **kwargs
        )
        super(RandomForestBalanced, self).__init__(name)

    def fit(self, x, y):
        self.model.fit(x, y)

    def predict(self, x):
        return self.model.predict(x)

    def load(self, path):
        self.model.load(path)

    def save(self, path):
        self.model.save(path)


class RandomForestRegressor(Model):
    def __init__(self, x_metadata, name="rf_regressor", **kwargs):

        self.x_metadata = x_metadata
        self.rf_args = kwargs
        cat_features = self.x_metadata[self.x_metadata["type"] == "cat"]
        num_features = ~cat_features
        self.model = Pipeline(
            steps=[
                (
                    "pre_process",
                    get_numeric_categorical_preprocessor(
                        numeric_features=self.x_metadata[num_features][
                            "feature"
                        ],
                        categorical_features=self.x_metadata[cat_features][
                            "feature"
                        ],
                    ),
                ),
                ("model", SKRandomForestRegressor(**self.rf_args)),
            ]
        )
        super(RandomForestRegressor, self).__init__(name)

    def fit(self, x, y):
        self.model.fit(x, y)

    def predict(self, x):
        return self.model.predict(x)

    def load(self, path):
        self.model = joblib.load(path)

    def save(self, path):
        joblib.dump(self.model, path)


models = [
    ("rf", RandomForest),
    ("rf_balanced", RandomForestBalanced),
    ("rf_regressor", RandomForestRegressor),
]
