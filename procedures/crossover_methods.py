import numpy as np


def create_circle_son(son, radius, mid):
    radius = radius * 1.5
    x_position = np.random.uniform(-1 * radius, radius)
    y_limit = np.sqrt(radius ** 2 - x_position ** 2)
    son.position[0] = mid[0] + x_position
    y_position = np.random.uniform(-1 * y_limit, y_limit)
    son.position[1] = mid[1] + y_position
    return son


def create_circle_son2(son, radius, mid):
    radius = radius * 1.5
    son.position[0] = np.random.uniform(0, radius)
    son.position[1] = 0  # só para garantir
    theta = np.radians(np.random.uniform(0, 360))
    c, s = np.cos(theta), np.sin(theta)
    M = np.array(((c, -s), (s, c)))
    son.position = M.dot(son.position)
    son.position = mid + son.position
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
    if radius < genetic_algorithm.radius_limit:
        radius = genetic_algorithm.radius_limit
    son1 = create_circle_son2(son1, radius, mid)
    son1 = add_parents(son1, dad, mom)
    son2 = create_circle_son2(son2, radius, mid)
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
