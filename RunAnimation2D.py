import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from SetVariables import *
from Objects.GeneticAlgorithm import GeneticAlgorithm
from Objects.Population import Population
from Procedures.DoOneGeneration import doOneGeneration
from Procedures.MakeHistogram import makeHistogram
from Procedures.VerifyIfChromossomesAreEqual import verifyIfChromossomesAreEqual

# creating project
geneticAlgorithm = GeneticAlgorithm(iterations, chromossomesNumber, standartDeviation, mutationChance, function,
                                    crossoverMethod, crossoverChance)
# creating population
population = Population(geneticAlgorithm.createChromossomes())
population.updateChromossomesInformations(geneticAlgorithm)


def animation2D(frame):
    global scat2D
    limits = geneticAlgorithm.function.limits
    plt.xlim(limits[0]-1, limits[1]+1)
    plt.ylim(limits[0]-1, limits[1]+1)
    scat2D.remove()
    positions = population.chromossomesInformations
    scat2D = plt.scatter(positions[::3], positions[1::3], c = ['k'])
    doOneGeneration(geneticAlgorithm, population)
    population.updateChromossomesInformations(geneticAlgorithm)
    geneticAlgorithm.iterations -= 1
    plt.title('generations left: %d' % (geneticAlgorithm.iterations+1))
    if geneticAlgorithm.iterations == -1 or verifyIfChromossomesAreEqual(population, geneticAlgorithm.function):
        anim.event_source.stop()
        makeHistogram(geneticAlgorithm, population)


scat2D = plt.scatter(0, 0)
anim = FuncAnimation(plt.gcf(), animation2D, interval=animationVelocity, repeat=False)  # inicia animação
plt.show()