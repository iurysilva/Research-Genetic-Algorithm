import numpy as np


class Chromossome:
    def __init__(self):
        self.position = 0
        self.fitness = 0

    def generate_random_position(self, function):
        limits = function.limits
        self.position = np.array(np.random.uniform(limits[0], limits[1]+1, function.dimensions), dtype="float64")

    def update_fitness(self, function):
        self.fitness = function.result(self.position)

    def get_fitness(self):
        return self.fitness
