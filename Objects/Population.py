import numpy as np

class Population():
    def __init__(self,chromossomes=np.array([])):
        self.chromossomes = chromossomes
        self.chromossomesInformations = 0
        self.angles = 0

    def updateChromossomesInformations(self, geneticAlgorithm):
        self.chromossomesInformations = np.zeros(geneticAlgorithm.chromossomesNumber*(geneticAlgorithm.function.dimensions+1))
        for i in range(0, geneticAlgorithm.chromossomesNumber):
            chromossome = self.chromossomes[i]
            self.chromossomesInformations[i * 3] = chromossome.position[0]
            self.chromossomesInformations[i * 3 + 1] = chromossome.position[1]
            self.chromossomesInformations[i * 3 + 2] = chromossome.fitness
