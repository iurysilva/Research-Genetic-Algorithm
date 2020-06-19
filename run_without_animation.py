from objects import GeneticAlgorithm
from objects import Population
from set_variables import *
from procedures import do_one_generation
from procedures import make_histogram


# creating project
geneticAlgorithm = GeneticAlgorithm(iterations, chromossomes_number, standart_deviation, mutation_chance, function,
                                    crossover_method, crossover_chance)
# creating population
population = Population(geneticAlgorithm.create_chromossomes())
population.update_chromossomes_informations(geneticAlgorithm)

for generations in range(geneticAlgorithm.iterations):
    do_one_generation(geneticAlgorithm, population)
make_histogram(geneticAlgorithm, population)
