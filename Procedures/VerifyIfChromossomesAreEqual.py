import numpy as np

def verifyIfChromossomesAreEqual(population,function):
    for i in range(function.dimensions):
            aux = population.chromossomesInformations[i::function.dimensions+1]
            if np.max(aux) != np.min(aux):
                return False
    return True
