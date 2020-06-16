import numpy as np
import matplotlib.pyplot as plt


def make_histogram(genetic_algorithm, population):
    f_minimum = genetic_algorithm.function.functionMinimum
    best = population.chromossomes[0].position
    plt.clf()
    plt.title('Best position found: (X= %f, Y= %f)\n\n Function minimum: (X= %f, Y= %f)' % (best[0], best[1], f_minimum[0], f_minimum[1]))
    plt.xticks(np.arange(0, 361, 30))
    plt.hist(population.chromossomesAngles, 100)
    plt.show()
