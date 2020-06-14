import numpy as np

class Chromossome():
    def __init__(self):
        self.position= 0
        self.fitness= 0

    def generateRandomPosition(self,function): #Irá gerar as particulas em uma posição aleatória entre os limites
        self.position= np.array(np.random.uniform(function.limits[0],function.limits[1]+1,function.dimensions),dtype="float64")

    def updateFitness(self,function):
        self.fitness= function.result(self.position)

    def get_fitness(self):
        return self.fitness
