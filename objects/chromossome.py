import numpy as np


class Chromossome:
    def __init__(self):
        self.position = 0
        self.fitness = 0
        self.dad = 0
        self.mom = 0
        self.position_before_mutation = 0

    def generate_random_position(self, function):
        limits = np.copy(function.limits)
        self.position = np.array(np.random.uniform(limits[0], limits[1]+1, function.dimensions), dtype="float64")

    def update_fitness(self, function):
        self.fitness = function.result(self.position)

    def get_fitness(self):
        return self.fitness
