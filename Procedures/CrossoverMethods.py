import numpy as np


def arithmetic(geneticAlgorithm, son, dad, mom):
    r = np.random.uniform(0, 1, geneticAlgorithm.function.dimensions)
    son.position = dad.position*r+(1-r)*mom.position
    return son


def blx(geneticAlgorithm, son, dad, mom):
    for i in range(geneticAlgorithm.function.dimensions):
        if dad.position[i] >= mom.position[i]:
            higher = dad.position[i]+np.absolute(dad.position[i]*0.5)
            lower = mom.position[i]-np.absolute(mom.position[i]*0.5)
        else:
            lower = dad.position[i]-np.absolute(dad.position[i]*0.5)
            higher = mom.position[i]+np.absolute(mom.position[i]*0.5)
        while True:
            b = np.random.uniform(-0.5, 1.5)
            son.position[i]= dad.position[i]+(b*(mom.position[i]-dad.position[i]))
            if higher >= son.position[i] >= lower:
                break
    return son
