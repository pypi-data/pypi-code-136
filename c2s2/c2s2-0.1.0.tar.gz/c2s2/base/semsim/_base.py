import abc

import numpy as np


class SimilarityKernel(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def compute(self, patient_a, patient_b):
        """
        Calculate semantic similarity between patients.

        :param patient_a: HPO terms of first individual
        :param patient_b: HPO terms of second individual
        """
        pass


class SimilarityMatrixCreator:
    # TODO - possibly remove the entire class if the component looks redundant.

    def __init__(self, similarity_kernel: SimilarityKernel):
        """Constructor
        :param similarity_kernel: kernel to calculate similarity
        """
        self._similarity_kernel = similarity_kernel

    def calculate_matrix(self, patient_list):
        """Calculate the similarity matrix using a kernel function
        :param patient_list: could be a dataframe with a column of HPO ids as lists, a spark dataframe, phenopackets, etc
        """
        # here we need to implement a similarity function, can be phenomizer, or something else, for now, stub returns a random matrix
        similarity_matrix = np.zeros((len(patient_list), len(patient_list)))
        for i in range(len(patient_list)):  # this assumes a list of lists for now
            for j in range(len(patient_list)):  # double loop might not work for spark? --> can def be made more efficient, i.e. instead of loop through full matrix, only calculate for triangle of matrix
                similarity_matrix[i, j] = self._similarity_kernel.compute(patient_list[i], patient_list[j])
        return similarity_matrix

