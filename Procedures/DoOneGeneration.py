from Procedures.LimitSonPosition import limitSonPosition
from Procedures.FindAngle import findAngle
from Procedures.UpdateAngleList import updateAngleList
import numpy as np


def doOneGeneration(geneticAlgorithm, population):
    if geneticAlgorithm.function.dimensions == 2:
        updateAngleList(geneticAlgorithm, population)
    for creatingSon in range(geneticAlgorithm.chromossomesNumber):
        son = geneticAlgorithm.crossover(population)
        son = geneticAlgorithm.mutation(son)
        son = limitSonPosition(son, geneticAlgorithm.function)
        population.chromossomes = np.append(population.chromossomes, son)
    population.ordenateChromossomes()
    geneticAlgorithm.naturalSelection(population)
    population.updateChromossomesInformations(geneticAlgorithm)
