from procedures.crossover_methods import *
from objects.benchmark_functions import *
from objects import GeneticAlgorithm
from objects import Population
from run_options import run_without_animation
from run_options import run_animation_2d


crossover_chance = 0.80
mutation_chance = 0.20
standart_deviation = 3  # Will be used in the Gaussian Mutation
iterations = 100
function = Bukin6()  # Eggholder(), Sphere(), Bukin6() or Cross()
chromossomes_number = 100
crossover_method = arithmetic  # arithmetic
animation_velocity = 2000  # In millisecond's
animation = True

# creating project
genetic_algorithm = GeneticAlgorithm(iterations, chromossomes_number, standart_deviation, mutation_chance, function,
                                    crossover_method, crossover_chance)
# creating population
population = Population(genetic_algorithm.create_chromossomes())
population.update_chromossomes_informations(genetic_algorithm)

if animation:
    run_animation_2d(genetic_algorithm, population, animation_velocity)
else:
    run_without_animation(genetic_algorithm, population)
