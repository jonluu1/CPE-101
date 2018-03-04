import numpy as np
import math

def sum(arr):
    return np.sum(arr)

def index_of_smallest(arr):
    if len(arr) == 0:
        return -1
    else:
        return np.argmin(arr)

def nearest_origin(arr):
    if len(arr) == 0:
        return -1
    else:
        distToOrigin = []
        for i in arr:
            distToOrigin.append(math.sqrt(i.x ** 2 + i.y ** 2))
        return np.argmin(distToOrigin)