from procedures.crossover_methods import *
from objects.benchmark_functions import *


crossover_chance = 0.80
mutation_chance = 0.02
standart_deviation = 3  # Will be used in the Gaussian Mutation
iterations = 1000
function = Sphere()  # Eggholder(), Sphere(), Bukin6() or Cross()
chromossomes_number = 50
crossover_method = arithmetic  # blx or arithmetic
animation_velocity = 20  # In millisecond's
