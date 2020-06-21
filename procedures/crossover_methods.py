import numpy as np


def arithmetic(genetic_algorithm, son1, son2, dad, mom):
    r = np.random.uniform(0, 1, genetic_algorithm.function.dimensions)
    son1.position = dad.position*r+(1-r)*mom.position
    son1.dad = dad
    son1.mom = mom
    son2.position = mom.position*r+(1-r)*dad.position
    son2.dad = dad
    son2.mom = mom
    return np.array([son1, son2])


def blx(genetic_algorithm, son, dad, mom):
    for i in range(genetic_algorithm.function.dimensions):
        if dad.position[i] >= mom.position[i]:
            higher = dad.position[i]+np.absolute(dad.position[i]*0.5)
            lower = mom.position[i]-np.absolute(mom.position[i]*0.5)
        else:
            lower = dad.position[i]-np.absolute(dad.position[i]*0.5)
            higher = mom.position[i]+np.absolute(mom.position[i]*0.5)
        while True:
            b = np.random.uniform(-0.5, 1.5)
            son.position[i] = dad.position[i]+(b*(mom.position[i]-dad.position[i]))
            if higher >= son.position[i] >= lower:
                break
    return son
