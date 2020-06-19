from procedures.crossover_methods import *
from objects.benchmark_functions import *


crossoverChance = 0.80
mutationChance = 0.02
standartDeviation = 3  # Will be used in the Gaussian Mutation
iterations = 100
function = Sphere()  # Eggholder(), Sphere(), Bukin6() or Cross()
chromossomesNumber = 100
crossoverMethod = arithmetic  # blx or arithmetic
animationVelocity = 20  # In millisecond's
