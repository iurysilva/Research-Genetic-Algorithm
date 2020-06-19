import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from procedures import do_one_generation
from procedures import make_histogram
import numpy as np


scat2D = 0
anim = 0
genetic_algorithm = 0
population = 0


def animation2d(frame):
    global scat2D, genetic_algorithm, population
    limits = genetic_algorithm.function.limits
    plt.xlim(limits[0]-1, limits[1]+1)
    plt.ylim(limits[0]-1, limits[1]+1)
    scat2D.remove()
    positions = np.copy(population.chromossomes_informations)
    scat2D = plt.scatter(positions[::3], positions[1::3], c=['k'])
    do_one_generation(genetic_algorithm, population)
    genetic_algorithm.iterations -= 1
    plt.title('generations left: %d' % (genetic_algorithm.iterations+1))
    if genetic_algorithm.iterations == -1:
        anim.event_source.stop()
        make_histogram(genetic_algorithm, population)


def run_animation_2d(genetic_algorithm2, population2, animation_velocity):
    global scat2D, anim, genetic_algorithm, population
    genetic_algorithm = genetic_algorithm2
    population = population2
    scat2D = plt.scatter(0, 0)
    anim = FuncAnimation(plt.gcf(), animation2d, interval=animation_velocity, repeat=False)
    plt.show()
