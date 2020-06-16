from procedures.LimitSonPosition import limitSonPosition
from procedures.UpdateAngleList import updateAngleList
import numpy as np


def doOneGeneration(geneticAlgorithm, population):
    if geneticAlgorithm.function.dimensions == 2:
        updateAngleList(geneticAlgorithm, population)
    kids = np.array([])
    numberOfKidsCreated = 0
    while numberOfKidsCreated < geneticAlgorithm.chromossomesNumber:
        dad = geneticAlgorithm.selection(population)
        mom = geneticAlgorithm.selection(population)
        son = geneticAlgorithm.crossover(dad, mom)
        if son is False:
            kids = np.append(kids, dad)
            kids = np.append(kids, mom)
            numberOfKidsCreated += 2
        else:
            son = geneticAlgorithm.mutation(son)
            son = limitSonPosition(son, geneticAlgorithm.function)
            kids = np.append(kids, son)
            numberOfKidsCreated += 1
    population.chromossomes = np.concatenate((population.chromossomes, kids))
    population.ordenateChromossomes()
    geneticAlgorithm.naturalSelection(population)
    population.updateChromossomesInformations(geneticAlgorithm)
