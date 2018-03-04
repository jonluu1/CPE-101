import unittest
import data
import vector_math
import collisions


# Create unittest test objects
class TestCollisions(unittest.TestCase):

    def test_quadratic_formula_0(self):
        a = 0.0
        b = 1.0
        c = 2.0
        self.assertEqual(vector_math.quadForm(a, b, c), None)

    def test_quadratic_formula_1(self):
        a = 1.0
        b = 0.0
        c = 0.0
        self.assertAlmostEqual(vector_math.quadForm(a, b, c), 0)

    def test_quadratic_formula_2(self):
        a = 1.0
        b = 0.0
        c = -1.0
        self.assertListEqual(vector_math.quadForm(a, b, c), [1.0, -1.0])

    def test_sphere_intersection_0(self):
        point_ray = data.Point(-10.0, 0.0, 0.0)
        direction = data.Vector(1.0, 0.0, 0.0)
        ray = data.Ray(point_ray, direction)
        point0_sphere = data.Point(0.0, 2.0, 0.0)
        sphere0 = data.Sphere(point0_sphere, 1.0)
        self.assertEqual(collisions.sphere_intersection_point(ray, sphere0), None)

    def test_sphere_intersection_1(self):
        point_ray = data.Point(-10.0, 0.0, 0.0)
        direction = data.Vector(1.0, 0.0, 0.0)
        ray = data.Ray(point_ray, direction)
        point1_sphere = data.Point(0.0, 1.0, 0.0)
        sphere1 = data.Sphere(point1_sphere, 1.0)
        collision_point = collisions.sphere_intersection_point(ray, sphere1)
        self.assertEqual(collision_point, data.Point(10.0, 0.0, 0.0))

    def test_sphere_intersection_2(self):
        point_ray = data.Point(-10.0, 0.0, 0.0)
        direction = data.Vector(1.0, 0.0, 0.0)
        ray = data.Ray(point_ray, direction)
        point2_sphere = data.Point(0.0, 0.0, 0.0)
        sphere2 = data.Sphere(point2_sphere, 1.0)
        collision_points = collisions.sphere_intersection_point(ray, sphere2)
        self.assertAlmostEqual(collision_points.x, -1.0)
        self.assertAlmostEqual(collision_points.y, 0.0)
        self.assertAlmostEqual(collision_points.z, 0.0)

    def test_sphere_intersection_3(self):
        point_ray = data.Point(-2581.5873, 7307.182, -4513.9069)
        direction = data.Vector(2669.2004, -7638.7545, -83.06)
        ray = data.Ray(point_ray, direction)
        point_sphere = data.Point(-188.86, -50.360, -300.360)
        sphere = data.Sphere(point_sphere, 400)
        collision_point = collisions.sphere_intersection_point(ray, sphere)
        self.assertEqual(collision_point, None)

    def test_find_sphere_intersections_0(self):
        point_ray = data.Point(-10.0, 0.0, 0.0)
        direction = data.Vector(1.0, 0.0, 0.0)
        ray = data.Ray(point_ray, direction)
        point0_sphere = data.Point(0.0, 2.0, 0.0)
        sphere0 = data.Sphere(point0_sphere, 1.0)
        collision_points = collisions.find_intersection_points([sphere0], ray)
        self.assertListEqual(collision_points, [])


    def test_find_sphere_intersections_1(self):
        point_ray = data.Point(-10.0, 0.0, 0.0)
        direction = data.Vector(1.0, 0.0, 0.0)
        ray = data.Ray(point_ray, direction)
        point0_sphere = data.Point(0.0, 2.0, 0.0)
        sphere0 = data.Sphere(point0_sphere, 1.0)
        point1_sphere = data.Point(0.0, 1.0, 0.0)
        sphere1 = data.Sphere(point1_sphere, 1.0)
        point2_sphere = data.Point(0.0, 0.0, 0.0)
        sphere2 = data.Sphere(point2_sphere, 1.0)
        collision_points = collisions.find_intersection_points([sphere0, sphere1, sphere2], ray)
        self.assertEqual(collision_points[0], data.Point(10.0, 0.0, 0.0))
        self.assertEqual(collision_points[1], data.Point(-1.0, 0.0, 0.0))


# Run unittest
if __name__ == '__main__':
    unittest.main()