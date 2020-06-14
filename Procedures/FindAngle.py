import numpy as np


def findAngle(position):
    point = position
    if point[0] == 0 and point[1] == 0:
        return -1
    elif point[0] == 0:
        if point[1] > 0:
            return 90
        else:
            return 270
    else:
        coefficient = point[1]/point[0]
        if point[0] > 0 and point[1] < 0:
            return np.degrees(np.arctan(coefficient))+360
        elif point[0] < 0 and point[1] <= 0:
            return np.degrees(np.arctan(coefficient))+180
        elif point[0] < 0 and point[1] > 0:
            return np.degrees(np.arctan(coefficient))+180
        else:
            return np.degrees(np.arctan(coefficient))