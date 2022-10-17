from typing import List
from . import PopulationBasedHeuristics
from random import random, choice


class DifferentialEvolution(PopulationBasedHeuristics):
    """
    Differential Evolution Algorithm
    """
    
    def __init__(self, *args, **params):
        super().__init__(*args, **params)
        # Differential Evolution parameters
        self.f = params.get("f", 0.5)
        self.cr = params.get("cr", 0.8)
        # Types: rand-1, best-1, current-to-best-1, best-2, rand-2
        self.type = params.get("type", "rand-1")
        self.index_list = [i for i in range(self.population_size)]
        
        # Check if population has enough size
        if self.population_size <= 3:
            raise ValueError("""
            Population size is not valid. Population size
            must be greater than 3
            """)
        
    def mutation(self) -> List[dict]:
        """
        Mutation Heuristic

        - For each :math:`x_{i}` in population
            - Select :math:`x_{r_1}`, :math:`x_{r_2}`, :math:`x_{r_3}`,
              :math:`x_{r_4}` and :math:`x_{r_5}` such as
              :math:`r_1 \neq r_2 \neq r_3 \neq r_4 \neq r_5 \neq i`
            - i) Rand/1/bin :math:`m_i = x_{r_1} + F (x_{r_2} - x_{r_3})`
              ii) Best/1 :math:`m_i = x_{\text{best}} + F (x_{r_1} - x_{r_2})`
              iii) Current-to-best/1 :math:`m_i = x_{i} + F (x_{\text{best}} - x_{i}) + F(x_{r_1} - x_{r_2})`
              iv) Best/2 :math:`m_i = x_{\text{best}} + F (x_{r_1} - x_{r_2}) + F(x_{r_3} - x_{r_4})`
              v) Rand/2 :math:`m_i = x_{r_1} + F (x_{r_2} - x_{r_3}) + F(x_{r_4} - x_{r_5})`
            - add :math:`m_i` to Mutation Matrix
        :return list: Mutation Matrix
        """
        mutation_matrix: List[dict] = []
        if self.type == "rand-1":
            for i in range(self.population_size):
                # Get Different Random Indexes
                r1 = choice(list(set(self.index_list) - {i}))
                r2 = choice(list(set(self.index_list) - {i, r1}))
                r3 = choice(list(set(self.index_list) - {i, r1, r2}))
                # Get associated vectors
                x1 = self.population[r1]["x"]
                x2 = self.population[r2]["x"]
                x3 = self.population[r3]["x"]
                mutation_matrix.append(self.fix_ranges({"x": [x1[j] + self.f * (x2[j] - x3[j])
                                                              for j in range(self.dimension)]}))
        elif self.type == "best-1":
            # Get best vector
            x_best = self.get_best(self.population)
            for i in range(self.population_size):
                # Get Different Random Indexes
                r1 = choice(list(set(self.index_list) - {i, x_best["index"]}))
                r2 = choice(list(set(self.index_list) - {i, x_best["index"], r1}))
                # Get associated vectors
                x1 = self.population[r1]["x"]
                x2 = self.population[r2]["x"]
                mutation_matrix.append(self.fix_ranges({"x": [x_best["x"][j] + self.f * (x1[j] - x2[j])
                                                              for j in range(self.dimension)]}))
        elif self.type == "current-to-best-1":
            # Get best vector
            x_best = self.get_best(self.population)
            for i in range(self.population_size):
                x_current = self.population[i]["x"]
                # Get Different Random Indexes
                r1 = choice(list(set(self.index_list) - {i, x_best["index"]}))
                r2 = choice(list(set(self.index_list) - {i, x_best["index"], r1}))
                # Get associated vectors
                x1 = self.population[r1]["x"]
                x2 = self.population[r2]["x"]
                mutation_matrix.append(self.fix_ranges({"x": [
                    x_current[j] + self.f * (x_best["x"][j] - x_current[j]) + self.f * (x1[j] - x2[j])
                    for j in range(self.dimension)
                ]}))
        elif self.type == "best-2":
            # Get best vector
            x_best = self.get_best(self.population)
            for i in range(self.population_size):
                # Get Different Random Indexes
                r1 = choice(list(set(self.index_list) - {i, x_best["index"]}))
                r2 = choice(list(set(self.index_list) - {i, x_best["index"], r1}))
                r3 = choice(list(set(self.index_list) - {i, x_best["index"], r1, r2}))
                r4 = choice(list(set(self.index_list) - {i, x_best["index"], r1, r2, r3}))
                # Get associated vectors
                x1 = self.population[r1]["x"]
                x2 = self.population[r2]["x"]
                x3 = self.population[r3]["x"]
                x4 = self.population[r4]["x"]
                mutation_matrix.append(self.fix_ranges({"x": [
                    x_best["x"][j] + self.f * (x1[j] - x2[j]) + self.f * (x3[j] - x4[j])
                    for j in range(self.dimension)
                ]}))
        elif self.type == "rand-2":
            for i in range(self.population_size):
                # Get Different Random Indexes
                r0 = choice(list(set(self.index_list) - {i}))
                r1 = choice(list(set(self.index_list) - {i, r0}))
                r2 = choice(list(set(self.index_list) - {i, r0, r1}))
                r3 = choice(list(set(self.index_list) - {i, r0, r1, r2}))
                r4 = choice(list(set(self.index_list) - {i, r0, r1, r2, r3}))
                # Get associated vectors
                x0 = self.population[r0]["x"]
                x1 = self.population[r1]["x"]
                x2 = self.population[r2]["x"]
                x3 = self.population[r3]["x"]
                x4 = self.population[r4]["x"]
                mutation_matrix.append(self.fix_ranges({"x": [
                    x0[j] + self.f * (x1[j] - x2[j]) + self.f * (x3[j] - x4[j])
                    for j in range(self.dimension)
                ]}))
        else:
            raise TypeError("¡Differential Evolution variant type is not defined!")
        
        return mutation_matrix
    
    def recombination(self, mutation_matrix: List[dict]) -> List[dict]:
        """
        Recombination Heuristic

        - For each :math:`x_i` in population
            - Select random number :math:`\text{rnd}` in :math:`[0, 1]`
            - Select random population index :math:`\text{rnd}_{index}`
            - Select random :math:`x_r`, :math:`v_r` from population and mutation matrix
            - For each :math:`x_{i,j}` in :math:`x_{i}`
                - if :math:`\text{rnd} < \text{CR}` or :math:`j = \text{rnd_{index}}`,
                  :math:`u_{i,j} = v_{r,j}` else :math:`u_{i,j} = x_{r,j}`
            - add :math:`u_i` to Recombination Matrix
        :param list mutation_matrix: Mutation Matrix
        :return list: Recombination Matrix
        """
        recombination_matrix: List[dict] = []
        for i in range(self.population_size):
            xr = self.population[i]["x"]
            vr = mutation_matrix[i]["x"]
            recombination_matrix.append({"x": [
                vr[j] if random() <= self.cr or j == choice(self.index_list)
                else xr[j] for j in range(self.dimension)]})
        
        return self.evaluate_population(recombination_matrix)
    
    def selection(self, recombination_matrix: List[dict]) -> List[dict]:
        """
        Selection Heuristic

        - For each :math:`x_i` in population
            - Select best between :math:`x_i` and :math:`u_i` from population and recombination matrix
            - Add the best to the new population
        :param list recombination_matrix: Recombination Matrix
        :return list: Selection Matrix
        """
        return [self.comparison(recombination_matrix[i], self.population[i])
                for i in range(self.population_size)]
        
    def population_enhancement(self) -> None:
        """
        Population Enhancement Method
        :return None:
        """
        # Step 1: Mutation
        mutation_matrix = self.mutation()
        # Step 2: Recombination
        recombination_matrix = self.recombination(mutation_matrix)
        # Step 3: Selection
        self.population = self.selection(recombination_matrix)
        
    def stop_condition(self) -> bool:
        return False


if __name__ == "__main__":
    pass
