from typing import List
from .harmonySearch import HarmonySearch
from random import random


class ModifiedHarmonySearch(HarmonySearch):
    """
    Modified Harmony Search Algorithm

    In order to get the worst harmony of the current generation we use DEB conditions such as:

    :math:`x_{worst} = \text{arg} \min_{x \in S} -f(x)`

    where
    :math:`S = \left\lbrace x: \ g_{i}(x) \leq 0 and h_{i}(x) = 0 and x \in U \subset \mathbb{R}^{d} \right\rbrace`
    """

    @staticmethod
    def worst(xi: dict, xj: dict) -> dict:
        """
        Compares to vectors evaluating DEB conditions
        :param dict xi: Vector i
        :param dict xj: Vector j
        :return dict: Return best vector based on DEB conditions
        """
        svr_i = xi["gx"] + xi["hx"]
        svr_j = xj["gx"] + xj["hx"]
        if svr_i <= 0 and svr_j <= 0:
            if xi["fx"] < xj["fx"]:
                return xj
            else:
                return xi
        elif svr_i > 0 and svr_j > 0:
            if svr_i < svr_j:
                return xj
            else:
                return xi
        else:
            if svr_i <= 0:
                return xj
            else:
                return xi

    def get_worst(self, population: List[dict]) -> dict:
        """
        Gets the worst individual for a given population using DEB conditions
        :return dict: Worst individual
        """
        worst_index = 0
        pop = [{**population[j], "index": j} for j in range(len(population))]
        for i in range(1, len(population)):
            worst = self.worst(pop[worst_index], pop[i])
            worst_index = worst["index"]
        return pop[worst_index]

    def population_enhancement(self) -> None:
        """
        Population Enhancement Method
        :return None:
        """
        worst_index = self.get_worst(self.population)["index"]
        worst_harmony = self.population[worst_index]
        rnd = random()

        # Create new Harmony
        if rnd <= self.hcmr:
            rnd = random()
            new_harmony = self.create_from_population()
            if rnd <= self.par:
                new_harmony = self.add_noise(new_harmony)
            new_harmony = self.fix_ranges(new_harmony)
        else:
            new_harmony = self.create_individual()
        new_harmony = self.evaluate_individual(new_harmony)

        # Select best harmony between worst and new
        self.population[worst_index] = self.comparison(worst_harmony, new_harmony)


if __name__ == "__main__":
    pass
