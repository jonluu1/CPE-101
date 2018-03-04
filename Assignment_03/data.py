import utility


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        equality1 = utility.epsilon_equal(self.x, other.x)
        equality2 = utility.epsilon_equal(self.y, other.y)
        equality3 = utility.epsilon_equal(self.z, other.z)
        return equality1 and equality2 and equality3


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        equality1 = utility.epsilon_equal(self.x, other.x)
        equality2 = utility.epsilon_equal(self.y, other.y)
        equality3 = utility.epsilon_equal(self.z, other.z)
        return equality1 and equality2 and equality3


class Ray:
    def __init__(self, pt, dir):
        self.pt = pt
        self.dir = dir

    def __eq__(self, other):
        equality1 = utility.epsilon_equal(self.pt.x, other.pt.x)
        equality2 = utility.epsilon_equal(self.pt.y, other.pt.y)
        equality3 = utility.epsilon_equal(self.pt.z, other.pt.z)
        equality4 = utility.epsilon_equal(self.dir.x, other.dir.x)
        equality5 = utility.epsilon_equal(self.dir.y, other.dir.y)
        equality6 = utility.epsilon_equal(self.dir.z, other.dir.z)
        return equality1 and equality2 and equality3 and equality4 and equality5 and equality6


class Sphere:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __eq__(self, other):
        equality1 = utility.epsilon_equal(self.center.x, other.center.x)
        equality2 = utility.epsilon_equal(self.center.y, other.center.y)
        equality3 = utility.epsilon_equal(self.center.z, other.center.z)
        equality4 = utility.epsilon_equal(self.radius, other.radius)
        return equality1 and equality2 and equality3 and equality4