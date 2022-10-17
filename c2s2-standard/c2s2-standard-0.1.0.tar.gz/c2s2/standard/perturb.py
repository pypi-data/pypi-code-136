import random
import networkx as nx

from c2s2.base.perturb import Perturbation


class Imprecision(Perturbation):
    def __init__(self, number_of_terms_to_replace, hpo_graph):
        """Constructor
        :param number_of_terms_to_replace: number of HPO terms to replace by (grand)parent terms
        :param hpo_graph: the HPO graph
        """
        self._hpo_graph = hpo_graph
        self._number_of_terms_to_replace = number_of_terms_to_replace

    def perturb(self, patient_list):
        """Perturb the input data
        :param patient_list: could be a dataframe with a column of HPO ids as lists, a spark dataframe, phenopackets, etc
        """
        # execution time of this class for 131072 individuals: 7.0 seconds (excluding construction of HPO graph)
        new_patient_list = patient_list[:]
        for i in range(len(new_patient_list)):
            terms_to_replace = [new_patient_list[i][y] for y in sorted(random.sample(range(len(new_patient_list[i])),
                                                                                     self._number_of_terms_to_replace))]
            for term in terms_to_replace:
                all_ancestors = nx.ancestors(self._hpo_graph, term)
                new_term = random.sample(list(all_ancestors), 1)[0]
                new_patient_list[i] = [new_term if a == term else a for a in new_patient_list[i]]
        return new_patient_list

