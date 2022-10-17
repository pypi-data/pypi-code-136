import numpy as np

from ._base import SimilarityKernel


class DummySimilarityKernel(SimilarityKernel):
    """A dummy similarity kernel that returns a random similarity value in range [0, 1]."""

    def compute(self, patient_a, patient_b):
        return np.random.uniform(0, 1)
