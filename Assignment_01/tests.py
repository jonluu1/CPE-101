import unittest
import data

class TestData(unittest.TestCase):
    #Test Point One
    def test_points_1(self):
        testPoints1 = data.Point(0, 1.0, 2.0)
        self.assertEquals(testPoints1.x, 0)
        self.assertEquals(testPoints1.y, 1.0)
        self.assertEquals(testPoints1.z, 2.0)
    #Test Point Two
    def test_points_2(self):
        testPoints2 = data.Point(4.2, 7.8, 12.3)
        self.assertEquals(testPoints2.x, 4.2)
        self.assertEquals(testPoints2.y, 7.8)
        self.assertEquals(testPoints2.z, 12.3)
    #Test Vector 1
    def test_vector_1(self):
        testVector1 = data.Vector(0.0, 1.0, 2.0)
        self.assertEquals(testVector1.x, 0)
        self.assertEquals(testVector1.y, 1.0)
        self.assertEquals(testVector1.z, 2.0)
    #Test Vector 2
    def test_vector_2(self):
        testVector2 = data.Vector(7.7, 1.4, 6.8)
        self.assertEquals(testVector2.x, 7.7)
        self.assertEquals(testVector2.y, 1.4)
        self.assertEquals(testVector2.z, 6.8)
    #Test Ray 1
    def test_ray_1(self):
        testRay1_Point = data.Point(1, 2, 3)
        testRay1_Vector = data.Vector(1, 2, 3)
        testRay1 = data.Ray(testRay1_Point, testRay1_Vector)
        self.assertEquals(testRay1.point, testRay1_Point)
        self.assertEquals(testRay1.direction, testRay1_Vector)
        self.assertEquals(testRay1.point.x, 1)
        self.assertEquals(testRay1.point.y, 2)
        self.assertEquals(testRay1.point.z, 3)
        self.assertEquals(testRay1.direction.x, 1)
        self.assertEquals(testRay1.direction.y, 2)
        self.assertEquals(testRay1.direction.z, 3)
    #Test Ray 2
    def test_ray_2(self):
        testRay2_Point = data.Point(4.7, 8.3, 3.1)
        testRay2_Vector = data.Vector(1.6, 4.7, 7.6)
        testRay2 = data.Ray(testRay2_Point, testRay2_Vector)
        self.assertEquals(testRay2.point, testRay2_Point)
        self.assertEquals(testRay2.direction, testRay2_Vector)
        self.assertEquals(testRay2.point.x, 4.7)
        self.assertEquals(testRay2.point.y, 8.3)
        self.assertEquals(testRay2.point.z, 3.1)
        self.assertEquals(testRay2.direction.x, 1.6)
        self.assertEquals(testRay2.direction.y, 4.7)
        self.assertEquals(testRay2.direction.z, 7.6)
    #Test Sphere 1
    def test_sphere_1(self):
        testSphere1_Point = data.Point(1, 2, 3)
        testSphere1 = data.Shpere(testSphere1_Point, 10)
        self.assertEquals(testSphere1.point, testSphere1_Point)
        self.assertEquals(testSphere1.radius, 10)
        self.assertEquals(testSphere1.point.x, 1)
        self.assertEquals(testSphere1.point.y, 2)
        self.assertEquals(testSphere1.point.z, 3)
    #Test Sphere 2
    def test_sphere_2(self):
        testSphere2_Point = data.Point(11.7, 2.4, 4.5)
        testSphere2 = data.Shpere(testSphere2_Point, 12)
        self.assertEquals(testSphere2.point, testSphere2_Point)
        self.assertEquals(testSphere2.radius, 12)
        self.assertEquals(testSphere2.point.x, 11.7)
        self.assertEquals(testSphere2.point.y, 2,4)
        self.assertEquals(testSphere2.point.z, 4.5)

#Run Test
if __name__ == "__main__":
    unittest.main()


