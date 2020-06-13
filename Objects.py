import numpy as np
from Functions import *
from Crossing_Methods import *

class Population():
    def __init__(self):
        self.number_of_chromossomes=10
        self.dimensions= 2
        self.chromossomes= np.array([])
        self.function= Eggholder
        self.function_minimum= 0
        self.limits= np.array([-10,10],dtype="int64")
        self.chromossomes_informations= 0
        self.angles= 0
        self.crossing_method= BLX
        
    def find_fitness(self,x):
        return self.function(x,self)


class Chromossome():
    def __init__(self,limits,population):
        self.position= self.define_position(limits,population)
        self.fitness= population.find_fitness(self.position)

    def define_position(self,limits,population): #Irá gerar as particulas em uma posição aleatória entre os limites
        self.position= np.array(np.random.uniform(population.limits[0],population.limits[1]+1,population.dimensions),dtype="float64")
        return self.position

    def get_fitness(self):
        return self.fitness
