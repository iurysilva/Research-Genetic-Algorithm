def limit_son_position(son, function):
    inferior_limit = function.limits[0]
    superior_limit = function.limits[1]
    for i in range(function.dimensions):
        if son.position[i] < inferior_limit:
            son.position[i] = inferior_limit
        elif son.position[i] > superior_limit:
            son.position[i] = superior_limit
    return son
