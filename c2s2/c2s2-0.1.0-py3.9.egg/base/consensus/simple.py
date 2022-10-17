import numpy as np
from c2s2.base.cluster import ClusteringAlgorithm
from c2s2.base.perturb import Perturbation
from c2s2.base.semsim import SimilarityMatrixCreator

from ._base import ConsensusClustering


class SimpleConsensusClustering(ConsensusClustering):

    def __init__(self, k_clusters, n_resample,
                 sim_matrix_creator: SimilarityMatrixCreator,
                 perturb_method: Perturbation,
                 clustering_algorithm: ClusteringAlgorithm):
        """Constructor

        :param k_clusters: the upper limit of the clusters to investigate. The limit is included
        :param n_resample: number of times to resample/pertube the dataset
        :param sim_matrix_creator: the similarity matrix creator to calculate the phenotypic similarity matrix
                for patients
        :param perturb_method: the method to resample/perturb the input data for consensus clustering
        :param clustering_algorithm: the algorithm to cluster the patient data, i.e. KMeans, DBScan, etc

        """
        if k_clusters < 2:
            raise Exception("Number of clusters should at least be 2.")

        self.k_clusters = list(range(2, k_clusters + 1))
        self._n_resample = n_resample
        self._perturb_method = perturb_method
        self._clustering_algorithm = clustering_algorithm
        self._sim_matrix = sim_matrix_creator
        self.connectivity_matrix = None
        self.pac = None
        # TODO verify properties of sim_kernel, perturb_method, clustering_algorithm

    def consensus_cluster(self, patient_list):
        # CreateSimilarityMatrix for original patient_list?

        M = np.zeros((len(self.k_clusters), len(patient_list), len(patient_list)), dtype=float)

        for i, k in enumerate(self.k_clusters):
            for h in range(self._n_resample):
                perturbed_patient_list = self._perturb_method.perturb(patient_list)
                similarity_matrix = self._sim_matrix.calculate_matrix(perturbed_patient_list)
                clusters = self._clustering_algorithm.cluster(similarity_matrix, k)
                M[i, :, :] = M[i, :, :] + np.array([clusters == a for a in clusters], dtype=int)
                # update connectivity matrix M, triangular because symmetricas, where Mij = 1 means i and j are in the same cluster (clustering labels can be deleted now)
                # if we're not updating connectivity matrix M, we can also store them all and then collapse/average the Ms
                # early stopping? p-value using likelihood ratio?
        self.connectivity_matrix = M / self._n_resample
        # TODO - thresholds can be hyperparameters
        self.pac = np.mean((self.connectivity_matrix > 0.1) & (self.connectivity_matrix < 0.9), axis=(1, 2))

        # determine best clusters here
        # likelihood ratio test? as epsilon/convergence test
        # calculate some clustering metrics (PAC score?) to compare different fits between k_clusters
        return self
