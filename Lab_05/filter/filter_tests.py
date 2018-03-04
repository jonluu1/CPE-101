import unittest
import filter
import point


class TestCases(unittest.TestCase):

    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    def test_are_positive_1(self):
        l1 = filter.are_positive([1.0 ,2.0, 3.0])
        l2 = [1.0, 2.0, 3.0]
        self.assertListAlmostEqual(l1, l2)

    def test_are_positive_2(self):
        l1 = filter.are_positive([-1.0, 0.0, 1.0])
        l2 = [1.0]
        self.assertListAlmostEqual(l1, l2)

    def test_are_greater_1(self):
        l1 = filter.are_greater_than([0.0, 1.0, 2.0, 3.0], -1)
        l2 = [0.0, 1.0, 2.0, 3.0]
        self.assertListAlmostEqual(l1, l2)

    def test_are_greater_2(self):
        l1 = filter.are_greater_than([0.0, 1.0, 2.0, 3.0], 2)
        l2 = [3.0]
        self.assertListAlmostEqual(l1, l2)

    def are_in_first_quadrant_1(self):
        p1 = point.Point(0,0)
        p2 = point.Point(1, 1)
        p3 = point.Point(-1, 1)
        p4 = point.Point(-1, -1)
        p5 = point.Point(1, -1)
        l1 = filter.are_in_first_quadrant([p1, p2, p3, p4, p5])
        l2 = [p2]
        self.assertListAlmostEqual(l1, l2)

    def are_in_first_quadrant_2(self):
        p1 = point.Point(10, 10)
        p2 = point.Point(-10, -10)
        l1 = filter.are_in_first_quadrant([p1, p2])
        l2 = [p1]
        self.assertListAlmostEqual(l1, l2)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()