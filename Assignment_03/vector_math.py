import data
import math


def scale_vector(vector, scalar):
    x = vector.x * scalar
    y = vector.y * scalar
    z = vector.z * scalar
    return data.Vector(x, y, z)


def dot_vector(vector1, vector2):
    component1 = vector1.x * vector2.x
    component2 = vector1.y * vector2.y
    component3 = vector1.z * vector2.z
    return component1 + component2 + component3


def length_vector(vector):
    return math.sqrt((vector.x ** 2 + vector.y ** 2 + vector.z ** 2))


def normalize_vector(vector):
    magnitude = length_vector(vector)
    if magnitude == 0:
        return vector
    else:
        x = vector.x / magnitude
        y = vector.y / magnitude
        z = vector.z / magnitude
        return data.Vector(x, y, z)


def difference_point(point1, point2):#fix
    x = point1.x - point2.x
    y = point1.y - point2.y
    z = point1.z - point2.z
    return data.Vector(x, y, z)


def difference_vector(vector1, vector2):
    x = vector1.x - vector2.x
    y = vector1.y - vector2.y
    z = vector1.z - vector2.z
    return data.Vector(x, y, z)


def translate_point(point, vector):
    x = point.x + vector.x
    y = point.y + vector.y
    z = point.z + vector.z
    return data.Point(x, y, z)


def vector_from_to(from_point, to_point):
    x = to_point.x - from_point.x
    y = to_point.y - from_point.y
    z = to_point.z - from_point.z
    return data.Vector(x, y, z)

#Extra Functions

def quadForm(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if a == 0:
        return None
    if discriminant < 0:
        return None
    if discriminant == 0:
        return (-b + math.sqrt(discriminant)) / (2 * a)
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return [x1, x2]

def distForm(point1, point2):
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2 + (point1.z - point2.z) ** 2)
