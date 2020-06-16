from objects import GeneticAlgorithm
from objects import Population
from procedures import verifyIfChromossomesAreEqual
from SetVariables import *
from procedures import doOneGeneration
from procedures import makeHistogram

# creating project
geneticAlgorithm = GeneticAlgorithm(iterations, chromossomesNumber, standartDeviation, mutationChance, function,
                                    crossoverMethod, crossoverChance)
# creating population
population = Population(geneticAlgorithm.createChromossomes())
population.updateChromossomesInformations(geneticAlgorithm)

for generations in range(geneticAlgorithm.iterations):
    if verifyIfChromossomesAreEqual(population, geneticAlgorithm.function) is True:
        break
    else:
        doOneGeneration(geneticAlgorithm, population)
makeHistogram(geneticAlgorithm, population)
