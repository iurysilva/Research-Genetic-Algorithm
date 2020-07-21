import numpy as np


def do_one_generation(genetic_algorithm, population):
    kids = np.array([])
    number_of_kids_created = 0
    for creating_kids in range(genetic_algorithm.chromossomes_number//2):
        dad = genetic_algorithm.selection(population)
        mom = genetic_algorithm.selection(population)
        children = genetic_algorithm.crossover(dad, mom)
        if children is False:
            kids = np.append(kids, dad)
            kids = np.append(kids, mom)
        else:
            kids = np.concatenate((kids, children))
        number_of_kids_created += 2
    kids = genetic_algorithm.mutation(kids)
    genetic_algorithm.update_angle_method(genetic_algorithm, population, kids)
    population.chromossomes = np.concatenate((population.chromossomes, kids))
    population.ordenate_chromossomes()
    genetic_algorithm.natural_selection(population, number_of_kids_created)
    population.update_chromossomes_informations(genetic_algorithm)
