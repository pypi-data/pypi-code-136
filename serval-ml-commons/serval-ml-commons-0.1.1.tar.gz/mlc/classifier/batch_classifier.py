import numpy as np

from mlc.utils import cut_in_batch


class BatchClassifier:
    def __init__(self, classifier, n_batch=1, batch_size=None) -> None:
        self.classifier = (classifier,)
        self.n_batch = (n_batch,)
        self.batch_size = batch_size

    def predict_proba(self, x):
        x_batches = cut_in_batch(x, self.n_batch, self.batch_size)
        y_pred_batches = [
            self.classifier.predict_proba(x_l) for x_l in x_batches
        ]
        return np.concatenate(y_pred_batches)
