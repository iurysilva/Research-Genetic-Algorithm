import numpy as np
import matplotlib.pyplot as plt


def makeHistogram(geneticAlgorithm, population):
    fMinimum = geneticAlgorithm.function.functionMinimum
    best = population.chromossomes[0].position
    plt.clf()
    plt.title('Best position found: (X= %f, Y= %f)\n\n Function minimum: (X= %f, Y= %f)' % (best[0], best[1], fMinimum[0], fMinimum[1]))
    plt.xticks(np.arange(0, 361, 30))
    plt.hist(population.chromossomesAngles, 100)
    plt.show()
