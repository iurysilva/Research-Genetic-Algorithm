import numpy as np
from Objects.Chromossome import Chromossome

class Population():
    def __init__(self, chromossomes=np.array([])):
        self.chromossomes = chromossomes
        self.chromossomesInformations = 0
        self.chromossomesAngles = np.array([], dtype="float64")

    def updateChromossomesInformations(self, geneticAlgorithm):
        if type(self.chromossomesInformations) == int:
            self.chromossomesInformations = np.zeros(geneticAlgorithm.chromossomesNumber*(geneticAlgorithm.function.dimensions+1), dtype="float64")
        for i in range(geneticAlgorithm.chromossomesNumber):
            chromossome = self.chromossomes[i]
            self.chromossomesInformations[i * 3] = chromossome.position[0]
            self.chromossomesInformations[i * 3 + 1] = chromossome.position[1]
            self.chromossomesInformations[i * 3 + 2] = chromossome.fitness

    def ordenateChromossomes(self):
        self.chromossomes = sorted(self.chromossomes, key=Chromossome.get_fitness)
