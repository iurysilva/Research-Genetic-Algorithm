import numpy as np


def create_circle_son(son, radius, mid):
    radius = radius*1.5
    son.position[0] = np.random.uniform(-1 * radius, radius)
    y_limit = np.sqrt(radius ** 2 - son.position[0] ** 2)
    son.position[0] = mid[0] + son.position[0]
    son.position[1] = np.random.uniform(-1 * y_limit, y_limit)
    son.position[1] = mid[1] + son.position[1]
    module = np.sqrt((son.position[0] - mid[0]) ** 2 + (son.position[1] - mid[1]) ** 2)
    return son


def add_parents(son, dad, mom):
    son.dad = np.copy(dad.position)
    son.mom = np.copy(mom.position)
    return son


def arithmetic(genetic_algorithm, son1, son2, dad, mom):
    r = np.random.uniform(0, 1, genetic_algorithm.function.dimensions)
    son1.position = dad.position*r+(1-r)*mom.position
    son1 = add_parents(son1, dad, mom)
    son2.position = mom.position*r+(1-r)*dad.position
    son2 = add_parents(son2, dad, mom)
    return np.array([son1, son2])


def circle(genetic_algorithm, son1, son2, dad, mom):
    mid = (dad.position+mom.position)/2
    radius = np.sqrt(np.sum((dad.position-mid)**2))
    son1 = create_circle_son(son1, radius, mid)
    son1 = add_parents(son1, dad, mom)
    son2 = create_circle_son(son2, radius, mid)
    son2 = add_parents(son2, dad, mom)
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
