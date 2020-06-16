import numpy as np
from objects import Chromossome
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
        random_position_a = randint(0, self.chromossomesNumber-1)
        candidate_a = population.chromossomes[random_position_a]
        while True:
            random_position_b = randint(0, self.chromossomesNumber-1)
            candidate_b = population.chromossomes[random_position_b]
            if random_position_a != random_position_b:
                break
        if candidate_a.fitness >= candidate_b.fitness:
            return candidate_b
        else:
            return candidate_a

    def mutation(self, son):
        for i in range(0, len(son.position)):
            if random() < self.mutationChance:
                son.position[i] = son.position[i] + np.random.normal(0, 3)
        return son

    def crossover(self, dad, mom):
        son = Chromossome()
        son.position = np.zeros(self.function.dimensions, dtype="float64")
        if random() < self.crossoverChance:
            return self.crossoverMethod(self, son, dad, mom)
        else:
            return False

    def natural_selection(self, population):
        while len(population.chromossomes) != 50:
            population.chromossomes = np.delete(population.chromossomes, -1)


