import math
import numpy as np

def square_all(arr):
    return np.square(arr)

def add_n_all(arr, n):
    nparr = np.array(arr)
    return nparr + n

def distance_all(arr):
    output = []
    for i in arr:
        output.append(math.sqrt(i.x ** 2 + i.y ** 2))
    return output