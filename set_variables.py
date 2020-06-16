from procedures.crossover_methods import *
from objects.benchmark_functions import *

crossoverChance = 0.80
mutationChance = 0.02
standartDeviation = 3  # Will be used in the Gaussian Mutation
iterations = 1000
function = Cross()  # Eggholder(), Sphere(), Bukin6() or Cross()
chromossomesNumber = 50
crossoverMethod = arithmetic  # blx or arithmetic
animationVelocity = 20  # In millisecond's
