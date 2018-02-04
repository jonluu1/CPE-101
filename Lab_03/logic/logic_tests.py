import unittest
import logic


class TestCases(unittest.TestCase):
    def test_is_even_1(self):
        self.assertTrue(logic.is_even(2))
        self.assertFalse(logic.is_even(3))

    def test_in_interval(self):
        self.assertTrue(logic.in_an_interval(5))
        self.assertTrue(logic.in_an_interval(15))
        self.assertTrue(logic.in_an_interval(102))


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
