def are_positive(arr):
    pos = []
    i = 0
    while i < len(arr):
        if arr[i] > 0:
            pos.append(arr[i])
        i += 1
    return pos

def are_greater_than(arr, n):
    greater = []
    for i in arr:
        if i > n:
            greater.append(i)
    return greater

def are_in_first_quadrant(arr):
    quadOne = []
    for i in arr:
        if i.x > 0 and i.y > 0:
            quadOne.append(i)
    return quadOne