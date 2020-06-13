import numpy as np

def arithmetic_crossing(filho,pai,mae,population):
    for i in range(0,population.dimensions):
        r=np.random.uniform(0,1)
        filho.position[i]= pai.position[i]*r+(1-r)*mae.position[i]
    return filho

def BLX(filho,pai,mae,population):
    for j in range(0,population.dimensions):
        if pai.position[j]>=mae.position[j]:
            maior=pai.position[j]+np.absolute(pai.position[j]*0.5)
            menor=mae.position[j]-np.absolute(mae.position[j]*0.5)
        else:
            menor=pai.position[j]-np.absolute(pai.position[j]*0.5)
            maior=mae.position[j]+np.absolute(mae.position[j]*0.5)
        while True:
            b= np.random.uniform(-0.5,1.5)
            filho.position[j]= pai.position[j]+(b*(mae.position[j]-pai.position[j]))
            if filho.position[j]<=maior and filho.position[j]>=menor:
                break
    return filho
