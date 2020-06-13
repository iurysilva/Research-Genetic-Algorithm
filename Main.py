import numpy as np
import matplotlib.pyplot as plt
import random
from Functions import *
from Crossing_Methods import *
from matplotlib.animation import FuncAnimation
from  Objects import *

#variáceis para modificar
chance= 0.02
standart_deviation= 3
iterations= 100
animation_velocity= 20 #em milissegundos
function= Eggholder
chromossomes_number= 50
crossing_method= BLX #BLX or arithmetic_crossing

''' --------------------Genetic Algorithm--------------------'''
def create_chromossome(population): #cria os cromossomos
    for i in range(0,population.number_of_chromossomes):
        if i==0:
            population.chromossomes= np.array([Chromossome(population.limits,population)])
        else:
            population.chromossomes= np.insert(population.chromossomes,i,Chromossome(population.limits,population))



def selection(population):
    candidato_a= population.chromossomes[random.randint(0,population.number_of_chromossomes-1)]
    while True:
        candidato_b= population.chromossomes[random.randint(0,population.number_of_chromossomes-1)]
        if np.ndarray.any(candidato_b.position!=candidato_a.position):
            break
    if candidato_a.fitness>=candidato_b.fitness:
        return candidato_b
    else:
        return candidato_a

def mutation(filho):
    global chance, standart_deviation
    for i in range(0,len(filho.position)):
        if random.random()<=chance:
            filho.position[i]= filho.position[i]+np.random.normal(0,3)
    return filho

        
def crossing(population):
    pai= selection(population)
    mae= selection(population)
    filho= Chromossome(population.limits,population)
    filho.position= np.zeros(population.dimensions,dtype="float64")
    return population.crossing_method(filho,pai,mae,population)



def limit_son_position(filho,population):
    for k in range(population.dimensions):
        if filho.position[k]<population.limits[0]:
            filho.position[k]=population.limits[0]
        elif filho.position[k]>population.limits[1]:
            filho.position[k]= population.limits[1]
    filho.fitness= population.find_fitness(filho.position)
    return filho

        
def remove(population):
    population.chromossomes= sorted(population.chromossomes,key=Chromossome.get_fitness)
    for i in range(0,population.number_of_chromossomes):
        population.chromossomes= np.delete(population.chromossomes,-1)

''' --------------------animation--------------------'''

def animation2D(frame):
    global scat2D,iterations
    #animação para verificar o bias
    plt.xlim(population.limits[0]-1,population.limits[1]+1)
    plt.ylim(population.limits[0]-1,population.limits[1]+1)
    scat2D.remove()
    aux=population.chromossomes_informations
    scat2D = plt.scatter(aux[::3],aux[1::3],c =  ['k'])
    main(population)
    update_information_list(population)
    iterations-=1
    plt.title('iterações restantes: %d'%(iterations+1))
    if iterations==-1:
        anim.event_source.stop()
        histogram()



def histogram():
    plt.clf()
    maior=0
    for j in range(0,len(population.chromossomes)):
        if population.chromossomes[j].fitness>=population.chromossomes[maior].fitness:
            maior= j
    best= population.chromossomes[maior].position
    plt.title('best position found: (X= %f, Y= %f)\n\n Function Minimum: (X= %f, Y= %f)'%(best[0],best[1],population.function_minimum[0],population.function_minimum[1]))
    plt.xticks(np.arange(0,361,30))
    plt.hist(population.angles,100)




def find_angle(position):
    #Coleta o angulo feito pelo movimento da particula em graus
    point= position
    if point[0]==0 and point[1]==0:
        return(-1)
    elif point[0]==0:
        if point[1]>0:
            return 90
        else:
            return 270
    else:
        coefficient= point[1]/point[0]
        if point[0]>0 and point[1]<0:
            return (np.degrees(np.arctan(coefficient))+360)
        elif point[0]<0 and point[1]<=0:
            return (np.degrees(np.arctan(coefficient))+180)
        elif point[0]<0 and point[1]>0:
            return (np.degrees(np.arctan(coefficient))+180)
        else:
            return (np.degrees(np.arctan(coefficient)))

    

    
def update_information_list(population):
    #atualiza as posições x e y de cada particula na lista "particles_informations" no objeto Population
    for i in range(0,population.number_of_chromossomes):
        chromossome= population.chromossomes[i]
        population.chromossomes_informations[i*3]= chromossome.position[0]
        population.chromossomes_informations[i*3+1]= chromossome.position[1]
        population.chromossomes_informations[i*3+2]= chromossome.fitness


''' --------------------Main--------------------'''
def main(population):
    global cont_angle
    keep_going=False
    for i in range(population.dimensions):
        aux= population.chromossomes_informations[i::population.dimensions+1]
        if np.max(aux)!=np.min(aux):
            keep_going=True
    
        

    #pegando angulos da iteração
    if population.dimensions==2:
        for i in population.chromossomes:
            population.angles[cont_angle]= find_angle(i.position)
            cont_angle+=1
    if keep_going:
        for i in range(0,population.number_of_chromossomes):
            filho= crossing(population)
            filho= mutation(filho)
            filho= limit_son_position(filho,population)
            population.chromossomes= np.append(population.chromossomes,filho)
        remove(population)
        update_information_list(population)


cont_angle= 0
scat2D= plt.scatter(0,0)
population= Population()
population.crossing_method= crossing_method
population.number_of_chromossomes= chromossomes_number
population.function= function
population.function(np.array([1,2]),population)
create_chromossome(population)
population.chromossomes_informations= np.zeros(population.number_of_chromossomes*3,dtype="float64")
update_information_list(population)
population.angles= np.zeros(population.number_of_chromossomes*(iterations+1),dtype="float64")
anim= FuncAnimation(plt.gcf(),animation2D,interval=animation_velocity,repeat=False) #inicia animação
plt.show()
