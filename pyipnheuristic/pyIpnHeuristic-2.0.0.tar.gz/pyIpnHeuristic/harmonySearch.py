from . import PopulationBasedHeuristics
from random import random, choice, uniform


class HarmonySearch(PopulationBasedHeuristics):
    """
    Harmony Search Algorithm
    """
    
    def __init__(self, *args, **params):
        super().__init__(*args, **params)
        self.hcmr = params.get("hcmr", 0.95)
        self.par = params.get("par", 0.10)
        self.alpha = params.get("alpha", 1.)
        
    def create_from_population(self) -> dict:
        """
        Create New Harmony from the current population

        - For :math:`j` in :math:`[0, d]`
            - Select random :math:`x_{i,j}` from population
            - Get new harmony :math:`\text{new_harmony}_{i,j} = x_{i,j}`
        :return dict: New harmony
        """
        x = [self.population[i]["x"] for i in range(self.population_size)]
        return {
            "x": [
                choice([x[i][j] for i in range(self.population_size)])
                for j in range(self.dimension)
            ],
            "fx": None,
            "gx": None,
            "hx": None
        }
    
    def add_noise(self, harmony: dict) -> dict:
        """
        Add noise to a given harmony

        - For :math:`j` in :math:`[0, d]`
            - Set random number :math:`U` in :math:`[-1, 1]`
            - :math:`h_{i,j}` = :math:`x_{i,j} + e U`, :math:`e` in :math:`[0, 1]`
        :param dict harmony: Harmony
        :return dict: Noisy Harmony
        """
        harmony["x"] = [
            harmony["x"][j] + self.alpha * uniform(-1, 1)
            for j in range(self.dimension)
        ]
        return harmony
        
    def population_enhancement(self) -> None:
        """
        Population Enhancement Method
        :return None:
        """
        fx = [x["fx"] for x in self.population]
        worst_index = fx.index(max(fx))
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
        
    def stop_condition(self) -> bool:
        return False


if __name__ == "__main__":
    pass
