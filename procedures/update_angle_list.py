import numpy as np


def update_angle_list(genetic_algorithm, population):
    x = population.chromossomes_informations[::3]
    y = population.chromossomes_informations[1::3]
    new_angles = np.arctan2(y, x)*180/np.pi
    for yPosition in range(genetic_algorithm.chromossomes_number):
        if y[yPosition] < 0:
            new_angles[yPosition] += 360
    population.chromossomesAngles = np.concatenate((population.chromossomes_angles, new_angles))
