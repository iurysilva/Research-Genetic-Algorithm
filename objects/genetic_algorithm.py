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
        candidato_a = population.chromossomes[randint(0, self.chromossomesNumber - 1)]
        while True:
            candidato_b = population.chromossomes[randint(0, self.chromossomesNumber - 1)]
            if np.ndarray.any(candidato_b.position != candidato_a.position):
                break
        if candidato_a.fitness >= candidato_b.fitness:
            return candidato_b
        else:
            return candidato_a

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


