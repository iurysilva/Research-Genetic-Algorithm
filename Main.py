from Objects.GeneticAlgorithm import GeneticAlgorithm
from Objects.BenchmarkFunctions import *
from Objects.Population import Population
from Procedures.CrossoverMethods import *
from Procedures.LimitSonPosition import limitSonPosition
from Procedures.VerifyIfChromossomesAreEqual import verifyIfChromossomesAreEqual

animation_velocity = 20

crossoverChance = 0.80
mutationChance = 0.02
standartDeviation = 3
iterations = 100
function = Eggholder()
chromossomesNumber = 50
crossoverMethod = BLX

# creating project
geneticAlgorithm = GeneticAlgorithm(iterations, chromossomesNumber, standartDeviation, mutationChance, function,
                                    crossoverMethod, crossoverChance)
# creating population
population = Population(geneticAlgorithm.createChromossomes())
population.updateChromossomesInformations(geneticAlgorithm)

# iterations
for generations in range(geneticAlgorithm.iterations):
    if verifyIfChromossomesAreEqual(population, function) is True:
        break
    for creatingSon in range(geneticAlgorithm.chromossomesNumber):
        son = geneticAlgorithm.crossover(population)
        son = geneticAlgorithm.mutation(son)
        son = limitSonPosition(son, geneticAlgorithm.function)
        population.chromossomes = np.append(population.chromossomes, son)
    geneticAlgorithm.naturalSelection(population)
    population.updateChromossomesInformations(geneticAlgorithm)
print(population.chromossomes[0].position)

'''
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


def main(population):
    global cont_angle
    #pegando angulos da iteração
    if population.dimensions==2:
        for i in population.chromossomes:
            population.angles[cont_angle]= find_angle(i.position)
            cont_angle+=1


cont_angle= 0
scat2D= plt.scatter(0,0)
population.function(np.array([1,2]),population)
population.angles= np.zeros(population.number_of_chromossomes*(iterations+1),dtype="float64")
plt.show()
'''
