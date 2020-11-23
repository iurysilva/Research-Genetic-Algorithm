import matplotlib.pyplot as plt
from procedures.crossover_methods import *
from procedures.update_angle_methods import *
from procedures import make_histogram
from objects.benchmark_functions import *
from objects import GeneticAlgorithm
from objects import Population
from run_options import run_without_animation
from run_options import run_animation_2d
from run_options import prove_rotational_variance


run_purpose = 'bias'  # 'bias' or 'rotational_variance'
crossover_chance = 0.80
mutation_chance = 0.01
standart_deviation = 3  # Will be used in the Gaussian Mutation
radius_limit = 2  # Will be used in the circle crossover
chromossomes_number = 20
iterations = 500
executions_number = 20  # Used in rotational variance run_purpose
degrees_to_rotate = 360  # Used in rotational variance run_purpose
function = Ellipse()  # Eggholder(), Sphere(), Bukin6(), Booth() or Cross()
function.rotation_number = 0
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

if run_purpose == 'bias':
    if animation:
        run_animation_2d(genetic_algorithm, population, animation_velocity)
    else:
        run_without_animation(genetic_algorithm, population)
        make_histogram(genetic_algorithm, population)
elif run_purpose == 'rotational_variance':
    result = prove_rotational_variance(genetic_algorithm, executions_number, degrees_to_rotate)
    plt.ylim(0, 35000)
    plt.plot(np.arange(0, degrees_to_rotate), result)
    plt.show()
else:
    print('run_purpose not correctly defined')
