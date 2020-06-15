def limitSonPosition(son, function):
    inferiorLimit = function.limits[0]
    superiorLimit = function.limits[1]
    for i in range(function.dimensions):
        if son.position[i] < inferiorLimit:
            son.position[i] = inferiorLimit
        elif son.position[i] > superiorLimit:
            son.position[i] = superiorLimit
    son.updateFitness(function)
    return son
