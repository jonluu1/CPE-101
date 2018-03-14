import unittest
import convert


class TestConvert(unittest.TestCase):

    def test_convert_1(self):
        n = "0.001"
        self.assertAlmostEqual(convert.float_default(n), 0.001)

    def test_convert_2(self):
        n = "abcd"
        self.assertFalse(convert.float_default(n))


if __name__ == '__main__':
    unittest.main()