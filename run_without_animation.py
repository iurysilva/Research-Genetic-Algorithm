from objects import GeneticAlgorithm
from objects import Population
from procedures import verify_if_chromossomes_are_equal
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
    if verify_if_chromossomes_are_equal(population, geneticAlgorithm.function) is True:
        break
    else:
        do_one_generation(geneticAlgorithm, population)
make_histogram(geneticAlgorithm, population)
