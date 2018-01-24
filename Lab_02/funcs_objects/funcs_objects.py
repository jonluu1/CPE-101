import math

def distance(point1, point2):
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)

def circles_overlap(circle1, circle2):
    return distance(circle1.center, circle2.center) < circle1.radius + circle2.radius