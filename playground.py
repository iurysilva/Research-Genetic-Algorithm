from procedures.crossover_methods import *
from procedures.update_angle_methods import *
from objects.benchmark_functions import *
from objects import GeneticAlgorithm
from objects import Population
from run_options import run_without_animation
from run_options import run_animation_2d


crossover_chance = 0.80
mutation_chance = 0.02
standart_deviation = 3  # Will be used in the Gaussian Mutation
radius_limit = 2  # Will be used in the circle crossover
iterations = 1000
function = Sphere()  # Eggholder(), Sphere(), Bukin6() or Cross()
chromossomes_number = 50
crossover_method = circle  # arithmetic, circle
# arctan_with_parent_position, only_position or arccos_with_parent_position
update_angle_method = arctan_with_parent_position
animation_velocity = 20  # In millisecond's
animation = False

# creating project
genetic_algorithm = GeneticAlgorithm(iterations, chromossomes_number, standart_deviation, mutation_chance, function,
                                    crossover_method, update_angle_method, crossover_chance, radius_limit)
# creating population
population = Population(genetic_algorithm.create_chromossomes())
population.update_chromossomes_informations(genetic_algorithm)

if animation:
    run_animation_2d(genetic_algorithm, population, animation_velocity)
else:
    run_without_animation(genetic_algorithm, population)
