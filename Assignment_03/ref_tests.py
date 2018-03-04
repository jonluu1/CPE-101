from data import *
from collisions import *
import unittest

class TestCollisions(unittest.TestCase):
   def test_sphere_intersection0(self):
      s = Sphere(Point(0.0, 2.0, 0.0), 1.0)
      so = Sphere(Point(0.0, 2.0, 0.0), 1.0)
      r = Ray(Point(0.0, 0.0, 0.0), Vector(0.0, 1.0, 0.0))
      ro = Ray(Point(0.0, 0.0, 0.0), Vector(0.0, 1.0, 0.0))
      sphere_intersection_point(r, s)
      self.assertEqual(s, so, 'Intersection 0: Input sphere modified.')
      self.assertEqual(r, ro, 'Intersection 0: Input ray modified.')


   def test_sphere_intersection1(self):
      s = Sphere(Point(0.0, 2.0, 0.0), 1.0)
      r = Ray(Point(0.0, 0.0, 0.0), Vector(0.0, 1.0, 0.0))
      self.assertEqual(sphere_intersection_point(r, s), Point(0.0, 1.0, 0.0),
         'Intersection 1: simple test along y-axis')


   def test_sphere_intersection2(self):
      s = Sphere(Point(0.0, 0.0, 0.0), 1.0)
      r = Ray(Point(0.0, 0.0, 0.0), Vector(1.0, 0.0, 0.0))
      self.assertEqual(sphere_intersection_point(r, s), Point(1.0, 0.0, 0.0),
         'Intersection 2: From within sphere at origin')


   def test_sphere_intersection3(self):
      s = Sphere(Point(1.0, 1.0, 0.0), 1.0)
      r = Ray(Point(0.0, 0.0, 0.0), Vector(0.2, 0.0, 0.0))
      self.assertEqual(sphere_intersection_point(r, s), Point(1.0, 0.0, 0.0),
         'Intersection 3: Single intersection point at <1,0,0>' +
         '\t watch for precision issues')


   def test_sphere_intersection4(self):
      s = Sphere(Point(2.0, 2.0, 0.0), 1.0)
      r = Ray(Point(0.0, 0.0, 0.0), Vector(1.0, 0.0, 0.0))
      self.assertEqual(sphere_intersection_point(r, s), None,
         'Intersection 4: Does not intersect.')


   def test_sphere_intersection5(self):
      s = Sphere(Point(0.0, 0.0, 0.0), 4.0)
      r = Ray(Point(0.0, 2.0, -4.0), Vector(0.658281, -0.557005, 0.506370))
      self.assertEqual(sphere_intersection_point(r, s),
         Point(0.47362624786864, 1.599239329218808, -3.635672117471643),
         'Intersection 5: Sphere at origin.  Ray through sphere.')


   def test_sphere_intersection6(self):
      s = Sphere(Point(0.0, -2.0, 0.0), 1.0)
      r = Ray(Point(0.0, 0.0, 0.0), Vector(0.0, 1.0, 0.0))
      self.assertEqual(sphere_intersection_point(r, s), None,
         'Intersection 6: Sphere \"behind\" ray.  No intersection.')


   def test_find_intersection_points0(self):
      spheres = [
         Sphere(Point(0.0, 2.0, 0.0), 1.0),
         Sphere(Point(0.0, 5.0, 0.0), 1.0),
         Sphere(Point(0.0, -4.0, 0.0), 1.0),
         Sphere(Point(0.0, 8.0, 0.0), 1.0)
         ]
      sphereso = [
         Sphere(Point(0.0, 2.0, 0.0), 1.0),
         Sphere(Point(0.0, 5.0, 0.0), 1.0),
         Sphere(Point(0.0, -4.0, 0.0), 1.0),
         Sphere(Point(0.0, 8.0, 0.0), 1.0)
         ]
      r = Ray(Point(0.0, 0.0, 0.0), Vector(0.0, 1.0, 0.0))
      ro = Ray(Point(0.0, 0.0, 0.0), Vector(0.0, 1.0, 0.0))
      find_intersection_points(spheres, r)
      self.assertEqual(spheres, sphereso, 'Find Intersection Points 0: Input list modified.')
      self.assertEqual(r, ro, 'Find Intersection Points 0: Input ray modified.')


   def test_find_intersection_points1(self):
      spheres = [
         Sphere(Point(0.0, 2.0, 0.0), 1.0),
         Sphere(Point(0.0, 5.0, 0.0), 1.0),
         Sphere(Point(0.0, -4.0, 0.0), 1.0),
         Sphere(Point(0.0, 8.0, 0.0), 1.0)
         ]
      r = Ray(Point(0.0, 0.0, 0.0), Vector(0.0, 1.0, 0.0))
      expected = [
         (Sphere(Point(0.0, 2.0, 0.0), 1.0), Point(0.0, 1.0, 0.0)),
         (Sphere(Point(0.0, 5.0, 0.0), 1.0), Point(0.0, 4.0, 0.0)),
         (Sphere(Point(0.0, 8.0, 0.0), 1.0), Point(0.0, 7.0, 0.0))
         ]
      self.assertEqual(find_intersection_points(spheres, r), expected,
         'Find Intersection Points 1: Hits three (of four) spheres.' +
         '\tThe order should match if directions were carefully followed.')


   def test_find_intersection_points2(self):
      spheres = [
         Sphere(Point(0.0, 2.0, 0.0), 1.0),
         Sphere(Point(0.0, 5.0, 0.0), 1.0),
         Sphere(Point(0.0, -4.0, 0.0), 1.0),
         Sphere(Point(0.0, 8.0, 0.0), 1.0)
         ]
      r = Ray(Point(0.0, 0.0, 0.0), Vector(0.0, 0.0, 1.0))
      expected = []
      self.assertEqual(find_intersection_points(spheres, r), expected,
         'Find Intersection Points 2: No hits.')


   def test_find_intersection_points3(self):
      spheres = []
      r = Ray(Point(0.0, 0.0, 0.0), Vector(0.0, 0.0, 1.0))
      expected = []
      self.assertEqual(find_intersection_points(spheres, r), expected,
         'Find Intersection Points 3: Empty spheres list.')

if __name__ == '__main__':
   unittest.main()
