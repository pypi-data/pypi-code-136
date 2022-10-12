from mlc.models.model import Model
from mlc.models.samples.sklearn_default import RandomForest as DefaultRf

rf_parameters = {
    "n_estimators": 125,
    "min_samples_split": 6,
    "min_samples_leaf": 2,
    "max_depth": 10,
    "bootstrap": True,
    "class_weight": "balanced",
}


class RandomForest(Model):
    def __init__(self, x_metadata, **kwargs):
        name = "rf_lcld"
        self.model = DefaultRf(
            x_metadata=x_metadata, **rf_parameters, **kwargs
        )

        super(RandomForest, self).__init__(name)

    def fit(self, x, y):
        self.model.fit(x, y)

    def predict(self, x):
        return self.model.predict(x)

    def load(self, path):
        self.model.load(path)

    def save(self, path):
        self.model.save(path)


models = [("rf_lcld", RandomForest)]
