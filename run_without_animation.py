from objects import GeneticAlgorithm
from objects import Population
from set_variables import *
from procedures import do_one_generation
from procedures import make_histogram


# creating project
geneticAlgorithm = GeneticAlgorithm(iterations, chromossomesNumber, standartDeviation, mutationChance, function,
                                    crossoverMethod, crossoverChance)
# creating population
population = Population(geneticAlgorithm.create_chromossomes())
population.update_chromossomes_informations(geneticAlgorithm)

for generations in range(geneticAlgorithm.iterations):
    do_one_generation(geneticAlgorithm, population)
make_histogram(geneticAlgorithm, population)
