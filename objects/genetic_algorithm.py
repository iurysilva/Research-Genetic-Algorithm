import numpy as np
from . import Chromossome
from random import *


class GeneticAlgorithm:
    def __init__(self, iterations, chromossomes_number, std, mutation_chance, function, crossover, angle, cross_chance, radius_limit):
        self.iterations = iterations
        self.standart_deviation = std
        self.mutation_chance = mutation_chance
        self.function = function
        self.crossover_method = crossover
        self.crossover_chance = cross_chance
        self.chromossomes_number = chromossomes_number
        self.update_angle_method = angle
        self.radius_limit = radius_limit

    def create_chromossomes(self):
        print("Created Chromossomes")
        chromossomes = np.array([])
        for i in range(self.chromossomes_number):
            chromossomes = np.append(chromossomes, Chromossome())
            chromossomes[i].generate_random_position(self.function)
            chromossomes[i].update_fitness(self.function)
        return chromossomes

    def tournament(self, candidate_a, candidate_b):
        winner = Chromossome()
        if candidate_a.fitness >= candidate_b.fitness:
            winner.position = np.copy(candidate_b.position)
        else:
            winner.position = np.copy(candidate_a.position)
        return winner

    def selection(self, population):
        random_position_a = randint(0, self.chromossomes_number-1)
        candidate_a = population.chromossomes[random_position_a]
        while True:
            random_position_b = randint(0, self.chromossomes_number-1)
            if random_position_a != random_position_b:
                candidate_b = population.chromossomes[random_position_b]
                break
        winner = self.tournament(candidate_a, candidate_b)
        return winner

    def mutation(self, kids):
        dimensions = self.function.dimensions
        for kid in kids:
            if random() < self.mutation_chance or type(kid.dad) == int or type(kid.mom) == int:
                kid.position = kid.position + np.random.normal(0, self.standart_deviation, dimensions)
        return kids

    def crossover(self, dad, mom):
        son1 = Chromossome()
        son2 = Chromossome()
        son1.position = np.zeros(self.function.dimensions, dtype="float64")
        son2.position = np.zeros(self.function.dimensions, dtype="float64")
        if random() < self.crossover_chance:
            return self.crossover_method(self, son1, son2, dad, mom)
        else:
            return False

    def natural_selection(self, population, number_of_kids_created):
        for _ in range(number_of_kids_created):
            population.chromossomes = np.delete(population.chromossomes, -1)