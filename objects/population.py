import numpy as np
from . import Chromossome


class Population:
    def __init__(self, chromossomes=np.array([])):
        self.chromossomes = chromossomes
        self.chromossomes_informations = 0
        self.chromossomes_angles = np.array([], dtype="float64")

    def update_chromossomes_informations(self, genetic_algorithm):
        if type(self.chromossomes_informations) == int:
            self.chromossomes_informations = np.zeros(genetic_algorithm.chromossomes_number*(genetic_algorithm.function.dimensions+1), dtype="float64")
        for i in range(genetic_algorithm.chromossomes_number):
            chromossome = self.chromossomes[i]
            self.chromossomes_informations[i * 3] = chromossome.position[0]
            self.chromossomes_informations[i * 3 + 1] = chromossome.position[1]
            self.chromossomes_informations[i * 3 + 2] = chromossome.fitness

    def ordenate_chromossomes(self):
        self.chromossomes = sorted(self.chromossomes, key=Chromossome.get_fitness)
