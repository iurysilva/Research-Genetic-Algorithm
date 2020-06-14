import numpy as np
from Objects.Chromossome import *
from random import *

class GeneticAlgorithm():
    def __init__(self,iterations,chromossomesNumber,std,mutationChance,function,crossover,crossChance):
        self.iterations= iterations
        self.standartDeviation= std
        self.mutationChance= mutationChance
        self.function= function
        self.crossoverMethod= crossover
        self.crossoverChance= crossChance
        self.chromossomesNumber= chromossomesNumber

    def createChromossomes(self):  # cria os cromossomos
        chromossomes= np.array([])
        for i in range(0,self.chromossomesNumber):
            chromossomes = np.append(chromossomes,Chromossome())
            chromossomes[i].generateRandomPosition(self.function)
            chromossomes[i].updateFitness(self.function)
        return chromossomes


    def selection(self,population):
        candidato_a = population.chromossomes[randint(0, self.chromossomesNumber - 1)]
        while True:
            candidato_b = population.chromossomes[randint(0, self.chromossomesNumber - 1)]
            if np.ndarray.any(candidato_b.position != candidato_a.position):
                break
        if candidato_a.fitness >= candidato_b.fitness:
            return candidato_b
        else:
            return candidato_a

    def mutation(self,son):
        for i in range(0, len(son.position)):
            if random() <= self.mutationChance:
                son.position[i] = son.position[i] + np.random.normal(0, 3)
        return son

    def crossover(self,population):
        dad = self.selection(population)
        mom = self.selection(population)
        son = Chromossome()
        son.position = np.zeros(self.function.dimensions, dtype="float64")
        return self.crossoverMethod(self, son, dad, mom)

    def naturalSelection(self,population):
        population.chromossomes = sorted(population.chromossomes, key=Chromossome.get_fitness)
        for i in range(0, self.chromossomesNumber):
            population.chromossomes = np.delete(population.chromossomes, -1)

