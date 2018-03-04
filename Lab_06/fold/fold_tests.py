import unittest
import fold
import point


class TestCases(unittest.TestCase):
    def test_sum_1(self):
        l = [0.0, 1.0, 2.0, 3.0]
        self.assertAlmostEqual(fold.sum(l), 6.0)

    def test_sum_2(self):
        l = [-1.0, 0.0, 1.0, 2.0]
        self.assertAlmostEqual(fold.sum(l), 2.0)

    def test_index_of_smallest_0(self):
        l = []
        self.assertEqual(fold.index_of_smallest(l), -1)

    def test_index_of_smallest_1(self):
        l = [100.0, 20.33, 21, 1]
        self.assertEqual(fold.index_of_smallest(l), 3)

    def test_index_of_smallest_2(self):
        l = [-100, 100.0, 20.33, 21, 1]
        self.assertEqual(fold.index_of_smallest(l), 0)

    def test_nearest_origin_0(self):
        l = []
        self.assertEqual(fold.nearest_origin(l), -1)

    def test_nearest_origin_1(self):
        point1 = point.Point(0.0, 0.0)
        point2 = point.Point(1.0, 1.0)
        point3 = point.Point(2.0, 2.0)
        l = [point1, point2, point3]
        self.assertEqual(fold.nearest_origin(l), 0)

    def test_nearest_origin_2(self):
        point1 = point.Point(0.0, 0.0)
        point2 = point.Point(1.0, 1.0)
        point3 = point.Point(2.0, 2.0)
        l = [point3, point1, point2]
        self.assertEqual(fold.nearest_origin(l), 1)

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
