import numpy as np

from c2s2.base.cluster import ClusteringAlgorithm
from sklearn import cluster


class DBScan(ClusteringAlgorithm):
    def cluster(self, similarity_matrix, k_clusters):
        """Cluster the similarity matrix
        :param similarity_matrix: the similarity matrix of the patients to cluster
        :param k_clusters: the number of clusters to form
        """
        DBSCANClusterer = cluster.DBSCAN(metric='precomputed')
        #DBSCAN implementation needs distance matrix, we have similarity, so lets flip distribution
        distance_matrix = np.max(similarity_matrix) - similarity_matrix
        DBSCANClusterer.fit(distance_matrix)
        return DBSCANClusterer.labels_


class SpectralClustering(ClusteringAlgorithm):
    def cluster(self, similarity_matrix, k_clusters):
        """Cluster the similarity matrix
        :param similarity_matrix: the similarity matrix of the patients to cluster
        :param k_clusters: the number of clusters to form
        """
        SpectralClusterer = cluster.SpectralClustering(n_clusters=k_clusters, affinity='precomputed')
        SpectralClusterer.fit(similarity_matrix)
        return SpectralClusterer.labels_

