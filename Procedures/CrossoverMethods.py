import numpy as np

def arithmetic_crossing(geneticAlgorithm, filho,pai,mae,population):
    for i in range(0,geneticAlgorithm.function.dimensions):
        r=np.random.uniform(0,1)
        filho.position[i]= pai.position[i]*r+(1-r)*mae.position[i]
    return filho

def BLX(geneticAlgorithm, son,dad,mom):
    for i in range(geneticAlgorithm.function.dimensions):
        if dad.position[i] >= mom.position[i]:
            higher = dad.position[i]+np.absolute(dad.position[i]*0.5)
            lower = mom.position[i]-np.absolute(mom.position[i]*0.5)
        else:
            lower = dad.position[i]-np.absolute(dad.position[i]*0.5)
            higher = mom.position[i]+np.absolute(mom.position[i]*0.5)
        while True:
            b = np.random.uniform(-0.5,1.5)
            son.position[i]= dad.position[i]+(b*(mom.position[i]-dad.position[i]))
            if son.position[i] <= higher and son.position[i] >= lower:
                break
    return son
