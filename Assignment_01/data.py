class Point:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

class Vector:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

class Ray:
    def __init__(self, point, direction):
        self.point = point
        self.direction = direction

class Shpere:
    def __init__(self, point, radius):
        self.point = point
        self.radius = float(radius)