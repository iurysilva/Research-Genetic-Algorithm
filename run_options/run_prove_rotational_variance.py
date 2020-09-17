from objects import Population
from run_options import run_without_animation
import numpy as np


def prove_rotational_variance(genetic_algorithm, executions_number, degrees):
    degree_average_list = np.array([], dtype='float64')
    for degree in range(degrees):
        genetic_algorithm.function.rotation_number = degree
        print('doing %d degree' % degree)
        distance_list = np.array([], dtype='float64')
        for execution in range(executions_number):
            population = Population(genetic_algorithm.create_chromossomes())
            run_without_animation(genetic_algorithm, population, True)
            distance = population.chromossomes[0].fitness - genetic_algorithm.function.function_minimum_fitness
            distance_list = np.append(distance_list, distance)
        degree_average_list = np.append(degree_average_list, np.sum(distance_list)/executions_number)
    return degree_average_list
