import re
from typing import Dict, Iterable, Sized, Union

import numpy as np

from ._base import SimilarityKernel

HPO_PATTERN = re.compile(r"HP:(?P<ID>\d{7})")


class TermPair:
    """A class to represent a pair of HPO terms."""

    @staticmethod
    def of(a: str, b: str):
        am = HPO_PATTERN.match(a)
        bm = HPO_PATTERN.match(b)
        if not (am and bm):
            raise ValueError(f"Invalid HPO terms a={a}, b={b}")
        return TermPair(int(am.group("ID")), int(bm.group("ID")))

    def __init__(self, a: int, b: int):
        """Create a TermPair from given HPO term IDs.

        :param a: ID of the first HPO term (e.g. 1234567 for `HP:1234567`)
        :param b: ID of the second HPO term (e.g. 1234567 for `HP:1234567`)
        """
        if a < b:
            self._t1 = a
            self._t2 = b
        else:
            self._t1 = b
            self._t2 = a

    @property
    def t1(self) -> str:
        """first HPO term
        :return:
        """
        return f"HP:{self._t1}"

    @property
    def t2(self) -> str:
        """second HPO term
        :return:
        """
        return f"HP:{self._t2}"

    def __eq__(self, other):
        return other and self.t1 == other.t1 and self.t2 == other.t2

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self._t1, self._t2))

    def __repr__(self):
        return f"TermPair(a={self._id_to_hpo_representation(self._t1)}, b={self._id_to_hpo_representation(self._t1)})"

    @staticmethod
    def _id_to_hpo_representation(term_id: int) -> str:
        """
        Turn the integral ID into an HPO CURIE (e.g. 1234 -> `HP:0001234`).
        """
        return 'HP:' + str(term_id).rjust(7, '0')


class Phenomizer(SimilarityKernel):

    def __init__(self, mica_dict: Dict[TermPair, float]):
        self._mica_dict = mica_dict

    def compute(self, patient_a: Union[Sized, Iterable[str]], patient_b: Union[Sized, Iterable[str]]):
        """" Calculate semantic similarity between patients using the Phenomizer algorithm
        :param patient_a: HPO terms of first individual
        :param patient_b: HPO terms of second individual
        """
        if len(patient_a) == 0 or len(patient_b) == 0:
            return 0.

        similarities = np.zeros(shape=(len(patient_a), len(patient_b)), dtype=float)
        for i, hpoA in enumerate(patient_a):
            for j, hpoB in enumerate(patient_b):
                tp = TermPair.of(hpoA, hpoB)
                similarities[i, j] = self._mica_dict.get(tp, 0.)

        max_a = np.max(similarities, axis=1)
        mean_a = max_a.mean()
        max_b = np.max(similarities, axis=0)
        mean_b = max_b.mean()
        return (mean_a + mean_b) * .5
