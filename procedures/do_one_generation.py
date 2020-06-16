from procedures.limit_son_position import limit_son_position
from procedures.update_angle_list import update_angle_list
import numpy as np


def do_one_generation(genetic_algorithm, population):
    if genetic_algorithm.function.dimensions == 2:
        update_angle_list(genetic_algorithm, population)
    kids = np.array([])
    number_of_kids_created = 0
    while number_of_kids_created < genetic_algorithm.chromossomesNumber:
        dad = genetic_algorithm.selection(population)
        mom = genetic_algorithm.selection(population)
        son = genetic_algorithm.crossover(dad, mom)
        if son is False:
            kids = np.append(kids, dad)
            kids = np.append(kids, mom)
            number_of_kids_created += 2
        else:
            son = genetic_algorithm.mutation(son)
            son = limit_son_position(son, genetic_algorithm.function)
            son.update_fitness(genetic_algorithm.function)
            kids = np.append(kids, son)
            number_of_kids_created += 1
    population.chromossomes = np.concatenate((population.chromossomes, kids))
    population.ordenate_chromossomes()
    genetic_algorithm.natural_selection(population)
    population.update_chromossomes_informations(genetic_algorithm)
