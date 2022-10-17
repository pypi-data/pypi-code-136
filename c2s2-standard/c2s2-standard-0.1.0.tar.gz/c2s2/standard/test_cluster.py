import unittest

import numpy as np

from .cluster import DBScan, SpectralClustering


class ClusteringTester(unittest.TestCase):

    def setUp(self):
        random_mat = np.random.uniform(0, 1, (100, 100))
        self._random_symmetric_mat = np.tril(random_mat) + np.tril(random_mat, -1).T
        assert (np.mean(self._random_symmetric_mat == self._random_symmetric_mat.T) == 1)
        self._k_clusters = np.random.randint(2, 10)

    def test_dbscan(self):
        cluster_labels = DBScan().cluster(self._random_symmetric_mat, self._k_clusters)
        assert(len(cluster_labels) == 100)
        assert(max(cluster_labels) < self._k_clusters)

    def test_spectralclustering(self):
        cluster_labels = SpectralClustering().cluster(self._random_symmetric_mat, self._k_clusters)
        assert(len(cluster_labels) == 100)
        assert(max(cluster_labels) < self._k_clusters)
