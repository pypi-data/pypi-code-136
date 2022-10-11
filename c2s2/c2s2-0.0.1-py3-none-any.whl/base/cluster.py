import abc

import numpy as np


class ClusteringAlgorithm(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def cluster(self, similarity_matrix, k_clusters):
        """Cluster the similarity matrix
        :param similarity_matrix: the similarity matrix of the patients to cluster
        :param k_clusters: the number of clusters to form
        """
        pass


class KMeans(ClusteringAlgorithm):

    def cluster(self, similarity_matrix, k_clusters):
        """Cluster the similarity matrix
        :param similarity_matrix: the similarity matrix of the patients to cluster
        :param k_clusters: the number of clusters to form
        """
        # implement clustering here, for stub, just return random assignments
        # TODO - implement or remove
        return np.random.randint(0, k_clusters, similarity_matrix.shape[0])
