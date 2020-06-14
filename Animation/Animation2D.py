import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



def animation2D(animation_velocity):
    anim = FuncAnimation(plt.gcf(), executing, interval=animation_velocity, repeat=False)  # inicia animação

def executing(frame):
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