import numpy as np
from . import Chromossome
from random import *


class GeneticAlgorithm:
    def __init__(self, iterations, chromossomes_number, std, mutation_chance, function, crossover, cross_chance):
        self.iterations = iterations
        self.standartDeviation = std
        self.mutationChance = mutation_chance
        self.function = function
        self.crossoverMethod = crossover
        self.crossoverChance = cross_chance
        self.chromossomesNumber = chromossomes_number

    def create_chromossomes(self):
        chromossomes = np.array([])
        for i in range(self.chromossomesNumber):
            chromossomes = np.append(chromossomes, Chromossome())
            chromossomes[i].generate_random_position(self.function)
            chromossomes[i].update_fitness(self.function)
        return chromossomes

    def selection(self, population):
        winner = Chromossome()
        random_position_a = randint(0, self.chromossomesNumber-1)
        candidate_a = population.chromossomes[random_position_a]
        while True:
            random_position_b = randint(0, self.chromossomesNumber-1)
            if random_position_a != random_position_b:
                candidate_b = population.chromossomes[random_position_b]
                break
        if candidate_a.fitness >= candidate_b.fitness:
            winner.position = np.copy(candidate_b.position)
        else:
            winner.position = np.copy(candidate_a.position)
        winner.update_fitness(self.function)
        return winner

    def mutation(self, kids):
        for kid in kids:
            for dimension in range(self.function.dimensions):
                if random() < self.mutationChance:
                    kid.position[dimension] = kid.position[dimension] + np.random.normal(0, 3)
                    kid.position[dimension] = self.make_chromossome_stay_on_bounds(kid.position[dimension])
                else:
                    kid.position[dimension] = self.make_chromossome_stay_on_bounds(kid.position[dimension])
        return kids

    def crossover(self, dad, mom):
        son1 = Chromossome()
        son2 = Chromossome()
        son1.position = np.zeros(self.function.dimensions, dtype="float64")
        son2.position = np.zeros(self.function.dimensions, dtype="float64")
        if random() < self.crossoverChance:
            return self.crossoverMethod(self, son1, son2, dad, mom)
        else:
            return False

    def natural_selection(self, population, number_of_kids_created):
        for removing in range(number_of_kids_created):
            population.chromossomes = np.delete(population.chromossomes, -1)

    def make_chromossome_stay_on_bounds(self, x_or_y):
        inferior_limit = self.function.limits[0]
        superior_limit = self.function.limits[1]
        if x_or_y < inferior_limit:
            return inferior_limit
        elif x_or_y > superior_limit:
            return superior_limit
        else:
            return x_or_y
