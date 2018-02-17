import unittest
import data
import vector_math


# Create unittest test objects
class TestData(unittest.TestCase):

    def test_point_1(self):
        p1 = data.Point(0.0, 1.0, 2.0)
        self.assertAlmostEqual(p1.x, 0.0)
        self.assertAlmostEqual(p1.y, 1.0)
        self.assertAlmostEqual(p1.z, 2.0)

    def test_point_2(self):
        p2 = data.Point(3.0, 4.0, 5.0)
        self.assertAlmostEqual(p2.x, 3.0)
        self.assertAlmostEqual(p2.y, 4.0)
        self.assertAlmostEqual(p2.z, 5.0)

    def test_point_equality_1(self):
        p1 = data.Point(1.0, 2.0, 3.0)
        p2 = data.Point(3.0, 4.0, 5.0)
        self.assertFalse(p1 == p2)

    def test_point_equality_2(self):
        p1 = data.Point(3.0, 4.0, 5.0)
        p2 = data.Point(3.0, 4.0, 5.0)
        self.assertTrue(p1 == p2)

    def test_vec_1(self):
        v = data.Vector(0.0, 1.0, 2.0)
        self.assertAlmostEqual(v.x, 0.0)
        self.assertAlmostEqual(v.y, 1.0)
        self.assertAlmostEqual(v.z, 2.0)

    def test_vec_2(self):
        v = data.Vector(3.0, 4.0, 5.0)
        self.assertAlmostEqual(v.x, 3.0)
        self.assertAlmostEqual(v.y, 4.0)
        self.assertAlmostEqual(v.z, 5.0)

    def test_vec_equality_1(self):
        v1 = data.Vector(0.0, 0.0, 0.0)
        v2 = data.Vector(0.0, 0.0, 0.0)
        self.assertTrue(v1 == v2)

    def test_vec_equality_2(self):
        v1 = data.Vector(0.0, 1.0, 2.0)
        v2 = data.Vector(3.0, 4.0, 5.0)
        self.assertFalse(v1 == v2)

    def test_ray_1(self):
        p = data.Point(0.0, 1.0, 2.0)
        v = data.Vector(3.0, 4.0, 5.0)
        r = data.Ray(p, v)
        self.assertAlmostEqual(r.pt.x, 0.0)
        self.assertAlmostEqual(r.pt.y, 1.0)
        self.assertAlmostEqual(r.pt.z, 2.0)
        self.assertAlmostEqual(r.dir.x, 3.0)
        self.assertAlmostEqual(r.dir.y, 4.0)
        self.assertAlmostEqual(r.dir.z, 5.0)

    def test_ray_2(self):
        p = data.Point(6.0, 7.0, 8.0)
        v = data.Vector(9.0, 10.0, 11.0)
        r = data.Ray(p, v)
        self.assertAlmostEqual(r.pt.x, 6.0)
        self.assertAlmostEqual(r.pt.y, 7.0)
        self.assertAlmostEqual(r.pt.z, 8.0)
        self.assertAlmostEqual(r.dir.x, 9.0)
        self.assertAlmostEqual(r.dir.y, 10.0)
        self.assertAlmostEqual(r.dir.z, 11.0)

    def test_ray_equality_1(self):
        p1 = data.Point(0.0, 1.0, 2.0)
        v1 = data.Vector(3.0, 4.0, 5.0)
        r1 = data.Ray(p1, v1)
        p2 = data.Point(0.0, 1.0, 2.0)
        v2 = data.Vector(3.0, 4.0, 5.0)
        r2 = data.Ray(p2, v2)
        self.assertTrue(r1 == r2)

    def test_ray_equality_2(self):
        p1 = data.Point(0.1, 1.0, 2.0)
        v1 = data.Vector(3.0, 4.0, 5.0)
        r1 = data.Ray(p1, v1)
        p2 = data.Point(0.0, 1.0, 2.0)
        v2 = data.Vector(3.0, 4.0, 5.0)
        r2 = data.Ray(p2, v2)
        self.assertFalse(r1 == r2)

    def test_sphere_1(self):
        p = data.Point(0.0, 1.0, 2.0)
        r = 3.0
        s = data.Sphere(p, r)
        self.assertAlmostEqual(s.center.x, 0.0)
        self.assertAlmostEqual(s.center.y, 1.0)
        self.assertAlmostEqual(s.center.z, 2.0)
        self.assertAlmostEqual(s.radius, 3.0)

    def test_sphere_2(self):
        p = data.Point(4.0, 5.0, 6.0)
        r = 7.0
        s = data.Sphere(p, r)
        self.assertAlmostEqual(s.center.x, 4.0)
        self.assertAlmostEqual(s.center.y, 5.0)
        self.assertAlmostEqual(s.center.z, 6.0)
        self.assertAlmostEqual(s.radius, 7.0)

    def test_sphere_equality_1(self):
        p1 = data.Point(0.0, 0.0, 0.0)
        r1 = 1.0
        s1 = data.Sphere(p1, r1)
        p2 = data.Point(0.0, 0.0, 0.0)
        r2 = 1.0
        s2 = data.Sphere(p2, r2)
        self.assertTrue(s1 == s2)

    def test_sphere_equality_2(self):
        p1 = data.Point(1.0, 0.0, 0.0)
        r1 = 1.0
        s1 = data.Sphere(p1, r1)
        p2 = data.Point(0.0, 0.0, 0.0)
        r2 = 1.0
        s2 = data.Sphere(p2, r2)
        self.assertFalse(s1 == s2)

    def test_scale_1(self):
        v = data.Vector(0.0, 0.1, 0.2)
        scale_factor = 1.5
        v_scaled = vector_math.scale_vector(v, scale_factor)
        self.assertEqual(v_scaled, data.Vector(0.0, 0.15, 0.3))
        self.assertAlmostEqual(v_scaled.x, 0.0)
        self.assertAlmostEqual(v_scaled.y, 0.15)
        self.assertAlmostEqual(v_scaled.z, 0.3)

    def test_scale_2(self):
        v = data.Vector(1.0, 2.0, 3.0)
        scale_factor = 1.5
        v_scaled = vector_math.scale_vector(v, scale_factor)
        self.assertEqual(v_scaled, data.Vector(1.5, 3.0, 4.5))
        self.assertAlmostEqual(v_scaled.x, 1.5)
        self.assertAlmostEqual(v_scaled.y, 3.0)
        self.assertAlmostEqual(v_scaled.z, 4.5)

    def test_dot_vector_1(self):
        v1 = data.Vector(1.0, 2.0, 3.0)
        v2 = data.Vector(1.0, 2.0, 3.0)
        dot_product = vector_math.dot_vector(v1, v2)
        self.assertAlmostEqual(dot_product, 14.0)

    def test_dot_vector_2(self):
        v1 = data.Vector(0.0, 0.0, 0.0)
        v2 = data.Vector(1.0, 2.0, 3.0)
        dot_product = vector_math.dot_vector(v1, v2)
        self.assertAlmostEqual(dot_product, 0.0)

    def test_length_1(self):
        v = data.Vector(0.0, 0.0, 0.0)
        length = vector_math.length_vector(v)
        self.assertAlmostEqual(length, 0.0)

    def test_length_2(self):
        v = data.Vector(3.0, 0.0, 4.0)
        length = vector_math.length_vector(v)
        self.assertAlmostEqual(length, 5.0)

    def test_normalize_1(self):
        v = data.Vector(0.0, 0.0, 0.0)
        v_normalized = vector_math.normalize_vector(v)
        self.assertEqual(v_normalized, data.Vector(0.0, 0.0, 0.0))
        self.assertAlmostEqual(v_normalized.x, 0.0)
        self.assertAlmostEqual(v_normalized.y, 0.0)
        self.assertAlmostEqual(v_normalized.z, 0.0)

    def test_normalize_2(self):
        v = data.Vector(3.0, 4.0, 0.0)
        v_normalized = vector_math.normalize_vector(v)
        self.assertEqual(v_normalized, data.Vector(0.6, 0.8, 0.0))
        self.assertAlmostEqual(v_normalized.x, 0.6)
        self.assertAlmostEqual(v_normalized.y, 0.8)
        self.assertAlmostEqual(v_normalized.z, 0.0)

    def test_difference_point_1(self):
        p1 = data.Point(0.0, 0.0, 0.0)
        p2 = data.Point(1.0, 2.0, 3.0)
        p3 = vector_math.difference_point(p1, p2)
        self.assertAlmostEqual(p3, data.Point(-1.0, -2.0, -3.0))
        self.assertAlmostEqual(p3.x, -1.0)
        self.assertAlmostEqual(p3.y, -2.0)
        self.assertAlmostEqual(p3.z, -3.0)

    def test_difference_point_2(self):
        p1 = data.Point(1.0, 2.0, 3.0)
        p2 = data.Point(1.0, 2.0, 3.0)
        p3 = vector_math.difference_point(p1, p2)
        self.assertAlmostEqual(p3, data.Point(0.0, 0.0, 0.0))
        self.assertAlmostEqual(p3.x, 0.0)
        self.assertAlmostEqual(p3.y, 0.0)
        self.assertAlmostEqual(p3.z, 0.0)

    def test_difference_vector_1(self):
        v1 = data.Vector(0.0, 0.0, 0.0)
        v2 = data.Vector(1.0, 2.0, 3.0)
        v3 = vector_math.difference_vector(v1, v2)
        self.assertAlmostEqual(v3.x, -1.0)
        self.assertAlmostEqual(v3.y, -2.0)
        self.assertAlmostEqual(v3.z, -3.0)

    def test_difference_vector_2(self):
        v1 = data.Vector(1.0, 2.0, 3.0)
        v2 = data.Vector(1.0, 2.0, 3.0)
        v3 = vector_math.difference_vector(v1, v2)
        self.assertAlmostEqual(v3.x, 0.0)
        self.assertAlmostEqual(v3.y, 0.0)
        self.assertAlmostEqual(v3.z, 0.0)

    def test_translate_point_1(self):
        p = data.Point(0.0, 0.0, 0.0)
        v = data.Vector(0.0, 0.0, 0.0)
        p_translated = vector_math.translate_point(p, v)
        self.assertEqual(p_translated, data.Point(0.0, 0.0, 0.0))
        self.assertAlmostEqual(p_translated.x, 0.0)
        self.assertAlmostEqual(p_translated.y, 0.0)
        self.assertAlmostEqual(p_translated.z, 0.0)

    def test_translate_point_2(self):
        p = data.Point(0.0, 0.0, 0.0)
        v = data.Vector(1.0, 2.0, 3.0)
        p_translated = vector_math.translate_point(p, v)
        self.assertEqual(p_translated, data.Point(1.0, 2.0, 3.0))
        self.assertAlmostEqual(p_translated.x, 1.0)
        self.assertAlmostEqual(p_translated.y, 2.0)
        self.assertAlmostEqual(p_translated.z, 3.0)

    def test_vector_from_to_1(self):
        p1 = data.Point(0.0, 0.0, 0.0)
        p2 = data.Point(1.0, 2.0, 3.0)
        v = vector_math.vector_from_to(p1, p2)
        self.assertEqual(v, data.Vector(1.0, 2.0, 3.0))

    def test_vector_from_to_2(self):
        p1 = data.Point(3.0, 2.0, 1.0)
        p2 = data.Point(1.0, 2.0, 3.0)
        v = vector_math.vector_from_to(p1, p2)
        self.assertAlmostEqual(v.x, -2.0)
        self.assertAlmostEqual(v.y, 0.0)
        self.assertAlmostEqual(v.z, 2.0)



# Run unittest
if __name__ == '__main__':
    unittest.main()