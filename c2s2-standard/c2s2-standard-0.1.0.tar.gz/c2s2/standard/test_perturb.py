import unittest

import networkx as nx

from .load_hpo_graph import get_hpo_graph_in_networkx
from .perturb import Imprecision


class TestPerturb(unittest.TestCase):

    def setUp(self) -> None:
        self._random_patient_list = [
            ['HP:0012520', 'HP:0002266', 'HP:0010651', 'HP:0020219', 'HP:0012379', 'HP:0007301', 'HP:0000098',
             'HP:0002926',
             'HP:0011195', 'HP:0001707', 'HP:0004323', 'HP:0011122', 'HP:0007598', 'HP:0010787', 'HP:0002286',
             'HP:0100818',
             'HP:0002121', 'HP:0001010', 'HP:0010719', 'HP:0000505', 'HP:0001533', 'HP:0000470', 'HP:0040195',
             'HP:0001508',
             'HP:0002373', 'HP:0000078', 'HP:0011360'],
            ['HP:0010866', 'HP:0003043', 'HP:0031567', 'HP:0000954', 'HP:0009811', 'HP:0020219', 'HP:0001881',
             'HP:0000846',
             'HP:0030311'],
            ['HP:0000774', 'HP:0012683', 'HP:0000078', 'HP:0012444', 'HP:0001155', 'HP:0100704', 'HP:0000014',
             'HP:0011804',
             'HP:0010987', 'HP:0002979', 'HP:0010787', 'HP:0001385', 'HP:0005120', 'HP:0003808', 'HP:0001421'],
            ['HP:0000914', 'HP:0025354', 'HP:0025032', 'HP:0001881', 'HP:0033725', 'HP:0011153', 'HP:0010787',
             'HP:0003474',
             'HP:0003272', 'HP:0001061'],
            ['HP:0025032', 'HP:0000486', 'HP:0000598', 'HP:0004324', 'HP:0010301', 'HP:0011014', 'HP:0011991',
             'HP:0011442',
             'HP:0007301', 'HP:0002143', 'HP:0001045', 'HP:0001260'],
            ['HP:0000733', 'HP:0001623', 'HP:0002861', 'HP:0001273', 'HP:0010647', 'HP:0010303', 'HP:0030972',
             'HP:0002013',
             'HP:0000951', 'HP:0007370', 'HP:0001435', 'HP:0002808', 'HP:0030791', 'HP:0001637', 'HP:0100491',
             'HP:0000256',
             'HP:0001519', 'HP:0005176', 'HP:0001334', 'HP:0002119'],
            ['HP:0002987', 'HP:0005445', 'HP:0001511', 'HP:0003764', 'HP:0001421', 'HP:0001483', 'HP:0002020',
             'HP:0000978',
             'HP:0011733', 'HP:0033353', 'HP:0012447', 'HP:0012646', 'HP:0002299', 'HP:0000765', 'HP:0001384',
             'HP:0003307',
             'HP:0005750', 'HP:0010307', 'HP:0000069', 'HP:0003336', 'HP:0012786', 'HP:0011123', 'HP:0000464',
             'HP:0002352'],
            ['HP:0000824', 'HP:0002650', 'HP:0000961', 'HP:0001072', 'HP:0040064']]
        self._hpo_graph = get_hpo_graph_in_networkx(
            "https://raw.githubusercontent.com/obophenotype/human-phenotype-ontology/master/hp.json")

    def test_imprecision(self):
        original_patient_list = self._random_patient_list[:]
        new_patient_list = Imprecision(number_of_terms_to_replace=3, hpo_graph=self._hpo_graph) \
            .perturb(original_patient_list)
        for i in range(len(original_patient_list)):
            for y in range(len(original_patient_list[i])):
                # now original_patient_list[i][y] is the original HPO term
                if original_patient_list[i][y] == new_patient_list[i][y]:
                    continue
                else:
                    ancestors_this_term = list(
                        nx.ancestors(self._hpo_graph, original_patient_list[i][y]))
                    assert (new_patient_list[i][y] in ancestors_this_term)
