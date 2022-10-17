from typing import List
from . import PopulationBasedHeuristics
from random import random, choice, uniform


class ArtificialBeeColony(PopulationBasedHeuristics):
    """
    Artificial Bee Colony Algorithm
    """

    def __init__(self, *args, **params):
        super().__init__(*args, **params)
        # Artificial Bee Colony parameters
        self.max_trials = params.get("max_trials", 2)
        self.mr = params.get("mr", 0.6)
        self.index_list = [i for i in range(self.population_size)]

    def new_vector(self, xi: dict, i: int) -> dict:
        """
        Generates new vector from a food source xi
        :param dict xi: Current food source
        :param int i: Current food source index
        :return dict: New food source
        """
        r = choice(list(set(self.index_list) - {i}))
        x_rand = self.population[r]
        return self.fix_ranges({
            "x": [xi["x"][j] + uniform(-1, 1) * (xi["x"][j] - x_rand["x"][j]) if random() < self.mr else xi["x"][j]
                  for j in range(self.dimension)]
        })

    def new_vector_from_best(self, xi: dict, x_best: dict) -> dict:
        """
        Generates new vector from a food source xi
        :param dict xi: Current food source
        :param dict x_best: The best current food source
        :return dict: New food source
        """
        return self.fix_ranges({
            "x": [xi["x"][j] + uniform(-1, 1) * (xi["x"][j] - x_best["x"][j]) if random() < self.mr else xi["x"][j]
                  for j in range(self.dimension)]
        })

    def smart_fight(self, xi: dict, x_best: dict, i: int):
        """
        Generates new vector from a food source xi and from a random vector
        :param dict xi: Current food source
        :param dict x_best: The best current food source
        :param int i: Current food source index
        :return dict: New food source
        """
        phi = random()
        r = choice(list(set(self.index_list) - {i}))
        x_rand = self.population[r]
        return self.fix_ranges({
            "x": [xi["x"][j] + phi * (x_rand["x"][j] - xi["x"][j]) +
                  (1 - phi) * (x_best["x"][j] - xi["x"][j])
                  for j in range(self.dimension)]
        })

    def mutation(self) -> List[dict]:
        """
        New candidate solutions generation
        :return List[dict]: Returns new candidate solutions
        """
        mutation_matrix: List[dict] = []
        for i in range(self.population_size):
            mutation_matrix.append(self.new_vector(self.population[i], i))
        return self.evaluate_population(mutation_matrix)

    @staticmethod
    def fit(x: dict) -> float:
        """
        Calculates food source fitness
        :param dict x: Current food source
        :return float: Food source fitness
        """
        if x["fx"] >= 0:
            return 1 / (1 + x["fx"])
        else:
            return 1 + abs(x["fx"])

    def probability(self, mutation_matrix) -> List[float]:
        """
        Calculates food source probability measure
        :return List[float]: Probability matrix for each food source
        """
        fitness_matrix = [self.fit(x) for x in mutation_matrix]
        return [fitness / sum(fitness_matrix) for fitness in fitness_matrix]

    def population_enhancement(self) -> None:
        """
        Population Enhancement Method
        :return None:
        """
        # Workers phase
        workers_mutation_matrix = self.mutation()
        for i in range(self.population_size):
            if self.comparison(self.population[i], workers_mutation_matrix[i])["x"] != self.population[i]["x"]:
                self.population[i] = {**workers_mutation_matrix[i], "trials": 0}
            else:
                self.population[i] = {
                    **self.population[i],
                    "trials": self.population[i].get("trials", 0) + 1
                }

        # Onlookers phase
        for i in range(self.population_size):
            best_x = self.get_best(self.population)
            new_x = self.evaluate_individual(self.new_vector_from_best(self.population[i], best_x))
            if self.comparison(self.population[i], new_x)["x"] != self.population[i]["x"]:
                self.population[i] = {**new_x, "trials": 0}
            else:
                self.population[i] = {
                    **self.population[i],
                    "trials": self.population[i].get("trials", 0) + 1
                }

        # Scouts Phase
        for i in range(self.population_size):
            if self.population[i].get("trials", 0) >= self.max_trials:
                x_best = self.get_best(self.population)
                new_x = self.evaluate_individual(self.new_vector_from_best(self.population[i], x_best))
                self.population[i] = {**new_x, "trials": 0}

    def stop_condition(self) -> bool:
        return False


if __name__ == "__main__":
    pass
