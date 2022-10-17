import abc
from random import sample

import numpy as np


class Perturbation(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def perturb(self, patient_list):
        # here perturb patient_data as part of consensus clustering to obtain stability of clusters
        pass


class NoPerturbation(Perturbation):
    def perturb(self, patient_list):
        """Perturb the input data
        :param patient_list: could be a dataframe with a column of HPO ids as lists, a spark dataframe, phenopackets, etc
        """
        return patient_list


class IncompletePhenotyping(Perturbation):
    def __init__(self, number_of_terms_per_patient):
        """Constructor
        :param number_of_terms_per_patient: number of HPO terms to downsample each individual to
        """
        self._number_of_terms_per_patient = number_of_terms_per_patient

    def perturb(self, patient_list):
        """Perturb the input data
        :param patient_list: could be a dataframe with a column of HPO ids as lists, a spark dataframe, phenopackets, etc
        """
        #execution time of this class for 131072 individuals: 1.3 seconds
        #if we decide on the data structure of patient_list, we can optimize this function by not looping over the lists of lists
        perturbed_data = np.zeros(len(patient_list), dtype=object)
        for i, patient in enumerate(patient_list):
            if len(patient) > self._number_of_terms_per_patient: #only do this when number of terms is larger dan number to downsample to
                perturbed_data[i] = np.random.choice(patient, self._number_of_terms_per_patient, replace=False)
            else:
                perturbed_data[i] = patient
        return perturbed_data


class NoiseAdding(Perturbation):
    def __init__(self, number_of_terms_to_add, nodes):
        """Constructor
        :param number_of_terms_to_add: number of HPO terms to add as random noise to each individual
        :param nodes: HPO terms to sample from to add the noise
        """
        self._hpo_terms = nodes
        self._number_of_terms_to_add = number_of_terms_to_add

    def perturb(self, patient_list):
        """Perturb the input data
        :param patient_list: could be a dataframe with a column of HPO ids as lists, a spark dataframe, phenopackets, etc
        """
        #execution time of this class for 131072 individuals: 0.3 seconds (excluding construction of HPO graph)
        selected_hpos = list(np.random.choice(self._hpo_terms, (len(patient_list), self._number_of_terms_to_add)))
        new_patient_list = [a + list(b) for a, b in zip(patient_list, selected_hpos)]
        return new_patient_list

