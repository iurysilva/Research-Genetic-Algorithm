import numpy as np


def verify_if_chromossomes_are_equal(population):
    first_x = np.copy(population.chromossomes_informations[0])
    first_y = np.copy(population.chromossomes_informations[1])
    for chromossome in population.chromossomes:
        if first_x != chromossome.position[0] or first_y != chromossome.position[1]:
            return False
    return True


def only_position(genetic_algorithm, population, kids):
    if verify_if_chromossomes_are_equal(population) is False:
        x = np.copy(population.chromossomes_informations[::3])
        y = np.copy(population.chromossomes_informations[1::3])
        new_angles = np.arctan2(y, x)*180/np.pi
        for yPosition in range(genetic_algorithm.chromossomes_number):
            if y[yPosition] < 0:
                new_angles[yPosition] += 360
        population.chromossomes_angles = np.concatenate((population.chromossomes_angles, new_angles))


def arctan_with_parents_position(genetic_algorithm, population, kids):
    pass