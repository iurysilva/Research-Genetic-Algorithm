import numpy as np


def angle_is_valid(r, kid):
    if type(kid.dad) == int:
        return False
    return True


def fix_angles(angles):
    for i in range(len(angles)):
        if angles[i] < 0:
            angles[i] += 360
    return angles


def add_angles_tan(new_angles, r, kid):
    if angle_is_valid(r, kid):
        angle = np.arctan2(r[1], r[0]) * 180 / np.pi
        new_angles = np.append(new_angles, angle)
    return new_angles


def add_angles_cos(new_angles, r, kid):
    if angle_is_valid(r, kid):
        x_axe = np.array([1, 0])
        scalar_product = np.dot(r, x_axe)
        module = np.sqrt(np.sum(r**2))
        if 1 >= scalar_product / module >= -1:
            angle = np.degrees(np.arccos(scalar_product / module))
            if r[1] < 0:
                angle = 360 - angle
            new_angles = np.append(new_angles, angle)
    return new_angles


def only_position(genetic_algorithm, population, kids):
    if genetic_algorithm.dimensions == 2:
        x = np.copy(population.chromossomes_informations[::3])
        y = np.copy(population.chromossomes_informations[1::3])
        new_angles = np.arctan2(y, x)*180/np.pi
        new_angles = fix_angles(new_angles)
        population.chromossomes_angles = np.concatenate((population.chromossomes_angles, new_angles))


def arctan_with_parent_position(genetic_algorithm, population, kids):
    new_angles = np.array([])
    if genetic_algorithm.function.dimensions == 2:
        for i in range(0, genetic_algorithm.chromossomes_number, 2):
            r1 = kids[i].position - kids[i].dad
            r2 = kids[i+1].position - kids[i+1].mom
            new_angles = add_angles_tan(new_angles, r1, kids[i])
            new_angles = add_angles_tan(new_angles, r2, kids[i+1])
        new_angles = fix_angles(new_angles)
        population.chromossomes_angles = np.concatenate((population.chromossomes_angles, new_angles))


def arccos_with_parent_position(genetic_algorithm, population, kids):
    new_angles = np.array([])
    if genetic_algorithm.function.dimensions == 2:
        for i in range(0, genetic_algorithm.chromossomes_number, 2):
            r1 = kids[i].position - kids[i].dad
            r2 = kids[i+1].position - kids[i+1].mom
            new_angles = add_angles_cos(new_angles, r1, kids[i])
            new_angles = add_angles_cos(new_angles, r2, kids[i+1])
        population.chromossomes_angles = np.concatenate((population.chromossomes_angles, new_angles))
