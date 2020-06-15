import numpy as np


def updateAngleList(geneticAlgorithm, population):
    x = population.chromossomesInformations[::3]
    y = population.chromossomesInformations[1::3]
    newAngles = np.arctan2(y, x)*180/np.pi
    for yPosition in range(geneticAlgorithm.chromossomesNumber):
        if y[yPosition] < 0:
            newAngles[yPosition] += 360
    population.chromossomesAngles = np.concatenate((population.chromossomesAngles, newAngles))
