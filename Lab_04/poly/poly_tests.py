import unittest
import poly

class TestPoly(unittest.TestCase):

    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    # Add tests here
    def test_poly(self):
        poly1 = [2.3, 4.7, 1.0]
        poly2 = [1.2, 2.1, -3.2]

        poly3 = poly.poly_add2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [3.5, 6.8, -2.2])

    def test_poly_add2(self):
        p1 = [0.0, 0.0, 0.0]
        p2 = [1.0, 2.0, 3.0]
        sum = poly.poly_add2(p1, p2)
        self.assertListAlmostEqual(sum, [1.0, 2.0, 3.0])

    def test_poly_mult2(self):
        p1 = [0.0, 0.0, 0.0]
        p2 = [1.0, 2.0, 3.0]
        product = poly.poly_mult2(p1, p2)
        self.assertListAlmostEqual(product, [0.0, 0.0, 0.0, 0.0, 0.0])

    def test_poly_mult2_1(self):
        p1 = [1.0, 1.0, 1.0]
        p2 = [1.0, 2.0, 3.0]
        product = poly.poly_mult2(p1, p2)
        self.assertListAlmostEqual(product, [1.0, 3.0, 6.0, 5.0, 3.0])


if __name__ == '__main__':
    unittest.main()
