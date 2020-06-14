from Procedures.FindAngle import findAngle
import numpy as np


def updateAngleList(geneticAlgorithm, population):
    if type(population.chromossomesAngles) == int:
        population.chromossomesAngles = np.zeros((geneticAlgorithm.iterations+1)*geneticAlgorithm.chromossomesNumber)
    for chromossome in population.chromossomes:
        population.chromossomesAngles[geneticAlgorithm.contAngle] = findAngle(chromossome.position)
        geneticAlgorithm.contAngle += 1
