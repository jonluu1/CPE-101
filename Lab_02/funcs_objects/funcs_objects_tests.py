import unittest
import objects
import funcs_objects

class TestCases(unittest.TestCase):
    def test_point(self):
        testPoint = objects.Point(0, 0)
        self.assertEquals(testPoint.x, 0)
        self.assertEquals(testPoint.y, 0)
        pass


    def test_circle(self):
        testPoint = objects.Point(0, 0)
        testCircle = objects.Circle(testPoint, 10)
        self.assertEquals(testCircle.center, testPoint)
        self.assertEquals(testCircle.center.x, testPoint.x)
        self.assertEquals(testCircle.center.y, testPoint.y)
        self.assertEquals(testCircle.radius, 10)
        pass

    # Add other testing functions
    def test_distance_1(self):
        point1 = objects.Point(0.0, 0.0)
        point2 = objects.Point(3.0, 4.0)
        self.assertAlmostEqual(funcs_objects.distance(point1, point2), 5.0)

    def test_distance_2(self):
        point1 = objects.Point(4.0, 6.0)
        point2 = objects.Point(7.0, 9.0)
        self.assertAlmostEqual(funcs_objects.distance(point1, point2), 4.24264068)

    def test_circles_overlap_1(self):
        point1 = objects.Point(0.0, 1.0)
        point2 = objects.Point(2.0, 3.0)
        circle1 = objects.Circle(point1, 3)
        circle2 = objects.Circle(point2, 6)
        self.assertTrue(funcs_objects.circles_overlap(circle1, circle2))

    def test_circles_overlap_2(self):
        point1 = objects.Point(1.0, 1.0)
        point2 = objects.Point(5.0, 10.0)
        circle1 = objects.Circle(point1, 3)
        circle2 = objects.Circle(point2, 2)
        self.assertFalse(funcs_objects.circles_overlap(circle1, circle2))

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

