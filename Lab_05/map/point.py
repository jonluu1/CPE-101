def epsilon_equal(n, m, epsilon=0.00001):
   return (n - epsilon) < m and (n + epsilon > m)

class Point:
   def __init__(self, x, y):
      self.x = x
      self.y = y

   def __eq__(self, other):
      return epsilon_equal(self.x, other.x) and epsilon_equal(self.y, other.y)
