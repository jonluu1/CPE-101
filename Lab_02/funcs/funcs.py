import math

def f(x):
    return 7 * x ** 2 + 2 * x

def g(x, y):
    return x ** 2 + y ** 2

def hypotenuse(a, b):
    return math.sqrt(g(a, b))

def is_positive(x):
    return x > 0