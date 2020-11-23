import numpy as np


def do_one_generation(genetic_algorithm, population):
    kids = np.array([])
    number_of_kids_created = 0
    for creating_kids in range(genetic_algorithm.chromossomes_number//2):
        dad = genetic_algorithm.selection(population)
        mom = genetic_algorithm.selection(population)
        children = genetic_algorithm.crossover(dad, mom)
        if children is False:
            dad.dad = False
            kids = np.append(kids, dad)
            mom.mom = False
            kids = np.append(kids, mom)
        else:
            kids = np.concatenate((kids, children))
        number_of_kids_created += 2
    kids = genetic_algorithm.mutation(kids)
    genetic_algorithm.update_angle_method(genetic_algorithm, population, kids)
    kids = make_chromossomes_stay_on_bounds(genetic_algorithm, kids)
    population.chromossomes = np.concatenate((population.chromossomes, kids))
    population.ordenate_chromossomes()
    genetic_algorithm.natural_selection(population, number_of_kids_created)
    population.update_chromossomes_informations(genetic_algorithm)


def make_chromossomes_stay_on_bounds(genetic_algorithm, kids):
    inferior_limit = genetic_algorithm.function.limits[0]
    superior_limit = genetic_algorithm.function.limits[1]
    for kid in kids:
        for dimension in range(genetic_algorithm.function.dimensions):
            if kid.position[dimension] < inferior_limit:
                kid.position[dimension] = inferior_limit
            elif kid.position[dimension] > superior_limit:
                kid.position[dimension] = superior_limit
        kid.update_fitness(genetic_algorithm.function)
    return kids
