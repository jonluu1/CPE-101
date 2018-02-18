from data import *
import unittest
from vector_math import *

class TestEquality(unittest.TestCase):
   def test_point(self):
      p = Point(1.0, 2.0, 3.0)
      self.assertTrue(p == Point(1.0, 2.0, 3.0))
      self.assertAlmostEqual(p.x, 1.0)
      self.assertAlmostEqual(p.y, 2.0)
      self.assertAlmostEqual(p.z, 3.0)
      self.assertFalse(Point(1.0, 2.0, 3.1) == Point(1.0, 2.0, 3.0))
      self.assertFalse(Point(1.0, 2.1, 3.0) == Point(1.0, 2.0, 3.0))
      self.assertFalse(Point(1.1, 2.0, 3.0) == Point(1.0, 2.0, 3.0))
      self.assertFalse(Point(1.0, 2.0, 3.0) == Point(1.0, 2.0, 3.1))
      self.assertFalse(Point(1.0, 2.0, 3.0) == Point(1.0, 2.1, 3.0))
      self.assertFalse(Point(1.0, 2.0, 3.0) == Point(1.1, 2.0, 3.0))
      self.assertFalse(Point(9.0, 0.0, 4.0) == Point(1.1, 2.0, 3.0))


   def test_vector(self):
      v = Vector(1.0, 2.0, 3.0)
      self.assertTrue(v == Vector(1.0, 2.0, 3.0))
      self.assertAlmostEqual(v.x, 1.0)
      self.assertAlmostEqual(v.y, 2.0)
      self.assertAlmostEqual(v.z, 3.0)
      self.assertFalse(Vector(1.0, 2.0, 3.1) == Vector(1.0, 2.0, 3.0))
      self.assertFalse(Vector(1.0, 2.1, 3.0) == Vector(1.0, 2.0, 3.0))
      self.assertFalse(Vector(1.1, 2.0, 3.0) == Vector(1.0, 2.0, 3.0))
      self.assertFalse(Vector(1.0, 2.0, 3.0) == Vector(1.0, 2.0, 3.1))
      self.assertFalse(Vector(1.0, 2.0, 3.0) == Vector(1.0, 2.1, 3.0))
      self.assertFalse(Vector(1.0, 2.0, 3.0) == Vector(1.1, 2.0, 3.0))
      self.assertFalse(Vector(9.0, 0.0, 4.0) == Vector(1.1, 2.0, 3.0))


   def test_ray(self):
      r = Ray(Point(1.0, 2.0, 3.0), Vector(4.0, 5.0, 6.0))
      self.assertTrue(r ==
         Ray(Point(1.0, 2.0, 3.0), Vector(4.0, 5.0, 6.0)))
      self.assertTrue(r.pt, Point(1.0, 2.0, 3.0))
      self.assertTrue(r.dir, Vector(4.0, 5.0, 6.0))
      self.assertFalse(
         Ray(Point(1.1, 2.0, 3.0), Vector(4.0, 5.0, 6.0)) ==
         Ray(Point(1.0, 2.0, 3.0), Vector(4.0, 5.0, 6.0)))
      self.assertFalse(
         Ray(Point(1.0, 2.0, 3.0), Vector(4.0, 5.0, 6.1)) ==
         Ray(Point(1.0, 2.0, 3.0), Vector(4.0, 5.0, 6.0)))


   def test_sphere(self):
      s = Sphere(Point(1.0, 2.0, 3.0), 3.0)
      self.assertTrue(s == Sphere(Point(1.0, 2.0, 3.0), 3.0))
      self.assertTrue(s.center, Point(1.0, 2.0, 3.0))
      self.assertTrue(s.radius, 3.0)
      self.assertFalse(
         Sphere(Point(1.0, 2.0, 3.0), 3.1) ==
         Sphere(Point(1.0, 2.0, 3.0), 3.0))
      self.assertFalse(
         Sphere(Point(1.0, 2.0, 3.0), 3.0) ==
         Sphere(Point(1.0, 2.1, 3.0), 3.0))


   def test_scale_0(self):
      v = Vector(2.7, 3.2, 4.1)
      s = scale_vector(v, 4.0)
      self.assertTrue(isinstance(s, Vector))
      self.assertEqual(v, Vector(2.7, 3.2, 4.1))


   def test_scale_1(self):
      self.assertEqual(scale_vector(Vector(2.7, 3.2, 4.1), 4.0),
         Vector(10.8, 12.8, 16.4))


   def test_scale_2(self):
      self.assertEqual(scale_vector(Vector(-1.2, 8.4, 0.0), -0.5),
         Vector(0.6, -4.2, 0.0))


   def test_dot_0(self):
      v1 = Vector(2.0, 0.0, 0.0)
      v2 = Vector(2.0, 0.0, 0.0)
      dot_vector(v1, v2)
      self.assertEqual(v1, Vector(2.0, 0.0, 0.0))
      self.assertEqual(v2, Vector(2.0, 0.0, 0.0))


   def test_dot_1(self):
      v1 = Vector(2.0, 0.0, 0.0)
      v2 = Vector(2.0, 0.0, 0.0)
      self.assertAlmostEqual(dot_vector(v1, v2), 4.0)


   def test_dot_2(self):
      v1 = Vector(2.7, 3.2, 4.1)
      v2 = Vector(-1.2, 8.4, 0.0)
      self.assertAlmostEqual(dot_vector(v1, v2), 23.64)


   def test_dot_3(self):
      v1 = Vector(1.0, 0.0, 0.0)
      v2 = Vector(0.0, 1.0, 0.0)
      self.assertAlmostEqual(dot_vector(v1, v2), 0.0)


   def test_length_0(self):
      v = Vector(2.0, 0.0, 0.0)
      length_vector(v)
      self.assertTrue(v == Vector(2.0, 0.0, 0.0))


   def test_length_1(self):
      v = Vector(2.0, 0.0, 0.0)
      self.assertAlmostEqual(length_vector(v), 2.0)


   def test_length_2(self):
      v = Vector(2.7, 3.2, 4.1)
      self.assertAlmostEqual(length_vector(v), 5.86003412959)


   def test_length_3(self):
      v = Vector(-1.2, 8.4, 0.0)
      self.assertAlmostEqual(length_vector(v), 8.48528137424)


   def test_normalize_0(self):
      v = Vector(1.0, 9.2, -8.0)
      n = normalize_vector(v)
      self.assertTrue(isinstance(n, Vector))
      self.assertEqual(v, Vector(1.0, 9.2, -8.0))


   def test_normalize_1(self):
      v = Vector(1.0, 1.0, 1.0)
      n = Vector(0.577350269189626, 0.577350269189626, 0.577350269189626)
      self.assertEqual(normalize_vector(v), n)


   def test_normalize_2(self):
      v = Vector(2.0, 0.0, 0.0)
      n = Vector(1.0, 0.0, 0.0)
      self.assertEqual(normalize_vector(v), n)


   def test_normalize_3(self):
      v = Vector(2.7, 3.2, 4.1)
      n = Vector(0.460748169770015, 0.54607190491261, 0.699654628169281)
      self.assertEqual(normalize_vector(v), n)


   def test_normalize_4(self):
      v = Vector(-1.2, 8.4, 0.0)
      n = Vector(-0.14142135623731, 0.989949493661167, 0.0)
      self.assertEqual(normalize_vector(v), n)


   def test_difference_0(self):
      p1 = Point(3.7, 4.2, 9.0)
      p2 = Point(2.0, 0.0, 0.0)
      v = difference_point(p1, p2)
      self.assertEqual(p1, Point(3.7, 4.2, 9.0))
      self.assertEqual(p2, Point(2.0, 0.0, 0.0))
      self.assertTrue(isinstance(v, Vector))


   def test_difference_1(self):
      p1 = Point(1.0, 1.0, 1.0)
      p2 = Point(2.0, 0.0, 0.0)
      v = Vector(-1.0, 1.0, 1.0)
      self.assertEqual(difference_point(p1, p2), v)


   def test_difference_2(self):
      p1 = Point(2.7, 3.2, 4.1)
      p2 = Point(-1.2, 8.4, 0.0)
      v = Vector(3.9, -5.2, 4.1)
      self.assertEqual(difference_point(p1, p2), v)


   def test_translate_0(self):
      p = Point(1.0, 1.1, 1.0)
      v = Vector(2.0, 0.0, 0.0)
      r = translate_point(p, v)
      self.assertEqual(p, Point(1.0, 1.1, 1.0))
      self.assertEqual(v, Point(2.0, 0.0, 0.0))
      self.assertTrue(isinstance(r, Point))


   def test_translate_1(self):
      p = Point(1.0, 1.0, 1.0)
      v = Vector(2.0, 0.0, 0.0)
      r = Point(3.0, 1.0, 1.0)
      self.assertEqual(translate_point(p, v), r)


   def test_translate_2(self):
      p = Point(2.7, 3.2, 4.1)
      v = Vector(-1.2, 8.4, 0.0)
      r = Point(1.5, 11.6, 4.1)
      self.assertEqual(translate_point(p, v), r)


   def test_difference_vector_0(self):
      v1 = Vector(4.2, 2.7, -10.4)
      v2 = Vector(9.3, -1.2, 0.4)
      v = difference_vector(v1, v2)
      self.assertEqual(v1, Vector(4.2, 2.7, -10.4))
      self.assertEqual(v2, Vector(9.3, -1.2, 0.4))
      self.assertTrue(isinstance(v, Vector))


   def test_difference_vector_1(self):
      v1 = Vector(4.2, 2.7, -10.4)
      v2 = Vector(9.3, -1.2, 0.4)
      self.assertEqual(difference_vector(v1, v2), Vector(-5.1, 3.9, -10.8))


   def test_difference_vector_2(self):
      v1 = Vector(4.2, 2.7, -10.4)
      v2 = Vector(-1.2, 8.4, 0.0)
      self.assertEqual(difference_vector(v1, v2), Vector(5.4, -5.7, -10.4))


   def test_difference_vector_3(self):
      v1 = Vector(-1.2, 8.4, 0.0)
      v2 = Vector(9.3, -1.2, 0.4)
      self.assertEqual(difference_vector(v1, v2), Vector(-10.5, 9.6, -0.4))


   def test_vector_from_to_0(self):
      p1 = Point(3.7, 4.2, 9.0)
      p2 = Point(2.0, 0.0, 0.0)
      v = vector_from_to(p2, p1)
      self.assertEqual(p1, Point(3.7, 4.2, 9.0))
      self.assertEqual(p2, Point(2.0, 0.0, 0.0))
      self.assertTrue(isinstance(v, Vector))


   def test_vector_from_to_1(self):
      p1 = Point(1.0, 1.0, 1.0)
      p2 = Point(2.0, 0.0, 0.0)
      self.assertEqual(vector_from_to(p2, p1), Vector(-1.0, 1.0, 1.0))


   def test_vector_from_to_2(self):
      p1 = Point(2.7, 3.2, 4.1)
      p2 = Point(-1.2, 8.4, 0.0)
      self.assertEqual(vector_from_to(p2, p1), Vector(3.9, -5.2, 4.1))



if __name__ == '__main__':
   unittest.main()
