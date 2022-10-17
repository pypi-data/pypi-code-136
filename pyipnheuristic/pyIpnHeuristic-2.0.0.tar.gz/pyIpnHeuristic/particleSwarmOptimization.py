from . import PopulationBasedHeuristics
from random import random, uniform


class ParticleSwarmOptimization(PopulationBasedHeuristics):
    """
    Particle Swarm Optimization Algorithm
    """

    def __init__(self, *args, **params):
        super().__init__(*args, **params)
        # Particle Swarm Optimization
        self.w = params.get("w", 0.1)
        self.c1 = params.get("c1", 0.2)
        self.c2 = params.get("c2", 0.2)
        # Initialize Population Velocity
        self.velocity = []
        self.particles_best_values = []

    def population_enhancement(self) -> None:
        """
        Population Enhancement Method
        :return None:
        """
        if len(self.velocity) == 0:
            self.velocity = [[uniform(-abs(max(ri) - min(ri)), abs(max(ri) - min(ri)))
                              for ri in self.ranges] for _ in self.population]
            self.particles_best_values = [particle for particle in self.population]

        # Get best vector
        g = self.get_best(self.population)

        # Calculate new particle velocity
        self.velocity = [
            [self.w * self.velocity[i][j] +
             self.c1 * random() * (self.particles_best_values[i]["x"][j] - self.population[i]["x"][j]) +
             self.c2 * random() * (g["x"][j] - self.population[i]["x"][j])
             for j in range(self.dimension)]
            for i in range(self.population_size)]

        # Calculate new particle position
        new_particles = self.evaluate_population([
            self.fix_ranges({
                "x": [self.population[i]["x"][j] + self.velocity[i][j] for j in range(self.dimension)]
            }) for i in range(self.population_size)])

        self.population = new_particles

        # Update particles best values
        self.particles_best_values = [self.comparison(self.particles_best_values[i], new_particles[i])
                                      for i in range(self.population_size)]

    def stop_condition(self) -> bool:
        return False


if __name__ == "__main__":
    pass
