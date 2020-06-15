from Objects.GeneticAlgorithm import GeneticAlgorithm
from Objects.Population import Population
from Procedures.VerifyIfChromossomesAreEqual import verifyIfChromossomesAreEqual
from SetVariables import *
from Procedures.DoOneGeneration import doOneGeneration
from Procedures.MakeHistogram import makeHistogram

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
