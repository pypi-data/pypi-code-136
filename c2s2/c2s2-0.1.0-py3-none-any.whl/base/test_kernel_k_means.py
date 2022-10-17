from unittest import TestCase
import numpy as np
from .cluster import KMeans
# adapted from https://github.com/National-COVID-Cohort-Collaborative/kernelkm/blob/master/src/test/
# test_k_means_and_gap_stat.py


class TestKMeans(TestCase):

    def setUp(self):
        # Make 6x6 matrix
        self._mat = np.array([[10, 5, 7, 1, 1, 1],  # Patient 1 similarities
                             [5, 10, 4, 1, 1, 1],  # Patient 2 similarities
                             [7, 4, 10, 1, 1, 1],  # Patient 3 similarities
                             [1, 1, 1, 10, 5, 5],  # Patient 4 similarities
                             [1, 1, 1, 5, 10, 5],  # Patient 5 similarities
                             [1, 1, 1, 5, 5, 10]])  # Patient 6 similarities
        self._kkm = KMeans(max_iter=100)

    def test_clustering(self):
        centroids, centroid_assignments, error = self._kkm.cluster(self._mat, k=2)
        self.assertEqual(centroid_assignments[0], centroid_assignments[1])