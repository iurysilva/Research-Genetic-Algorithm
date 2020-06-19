import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from set_variables import *
from objects import GeneticAlgorithm
from objects import Population
from procedures import do_one_generation
from procedures import make_histogram


# creating project
geneticAlgorithm = GeneticAlgorithm(iterations, chromossomesNumber, standartDeviation, mutationChance, function,
                                    crossoverMethod, crossoverChance)
# creating population
population = Population(geneticAlgorithm.create_chromossomes())
population.update_chromossomes_informations(geneticAlgorithm)


def animation2d(frame):
    global scat2D
    limits = geneticAlgorithm.function.limits
    plt.xlim(limits[0]-1, limits[1]+1)
    plt.ylim(limits[0]-1, limits[1]+1)
    scat2D.remove()
    positions = population.chromossomes_informations
    scat2D = plt.scatter(positions[::3], positions[1::3], c=['k'])
    do_one_generation(geneticAlgorithm, population)
    geneticAlgorithm.iterations -= 1
    plt.title('generations left: %d' % (geneticAlgorithm.iterations+1))
    if geneticAlgorithm.iterations == -1:
        anim.event_source.stop()
        make_histogram(geneticAlgorithm, population)


scat2D = plt.scatter(0, 0)
anim = FuncAnimation(plt.gcf(), animation2d, interval=animationVelocity, repeat=False)
plt.show()
