import numpy as np
from . import Chromossome


class Population:
    def __init__(self, chromossomes=np.array([])):
        self.chromossomes = chromossomes
        self.chromossomesInformations = 0
        self.chromossomesAngles = np.array([], dtype="float64")

    def update_chromossomes_informations(self, genetic_algorithm):
        if type(self.chromossomesInformations) == int:
            self.chromossomesInformations = np.zeros(genetic_algorithm.chromossomesNumber*(genetic_algorithm.function.dimensions+1), dtype="float64")
        for i in range(genetic_algorithm.chromossomesNumber):
            chromossome = self.chromossomes[i]
            self.chromossomesInformations[i * 3] = chromossome.position[0]
            self.chromossomesInformations[i * 3 + 1] = chromossome.position[1]
            self.chromossomesInformations[i * 3 + 2] = chromossome.fitness

    def ordenate_chromossomes(self):
        self.chromossomes = sorted(self.chromossomes, key=Chromossome.get_fitness)
