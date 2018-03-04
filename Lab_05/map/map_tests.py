import unittest
import map
import point


class TestCases(unittest.TestCase):

    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    def test_square_all_1(self):
        l1 = map.square_all([0.0, 1.0, 2.0])
        l2 = [0.0, 1.0, 4.0]
        self.assertListAlmostEqual(l1, l2)

    def test_square_all_2(self):
        l1 = map.square_all([-1.0, 0.0, 1.0])
        l2 = [1.0, 0.0, 1.0]
        self.assertListAlmostEqual(l1, l2)

    def test_add_n_all_1(self):
        l1 = map.add_n_all([0.0, 1.0, 2.0], 1)
        l2 = [1.0, 2.0, 3.0]
        self.assertListAlmostEqual(l1, l2)

    def test_add_n_all_2(self):
        l1 = map.add_n_all([0.0, 1.0, 2.0], -1)
        l2 = [-1.0, 0.0, 1.0]
        self.assertListAlmostEqual(l1, l2)

    def test_distance_all_1(self):
        p1 = point.Point(0.0, 0.0)
        p2 = point.Point(3.0, 4.0)
        p3 = point.Point(5.0, 12.0)
        l1 = map.distance_all([p1, p2, p3])
        l2 = [0.0, 5.0, 13.0]
        self.assertListAlmostEqual(l1, l2)

    def test_distance_all_2(self):
        p1 = point.Point(0.0, 0.0)
        p2 = point.Point(-3.0, 4.0)
        p3 = point.Point(5.0, -12.0)
        l1 = map.distance_all([p1, p2, p3])
        l2 = [0.0, 5.0, 13.0]
        self.assertListAlmostEqual(l1, l2)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()