import unittest
import funcs

class TestCases(unittest.TestCase):
    def test_f_1(self):
        self.assertEquals(funcs.f(1), 9)
        pass


    def test_f_2(self):
        self.assertEquals(funcs.f(0), 0)
        pass

    def test_g_1(self):
        self.assertEquals(funcs.g(1, 1), 2)
        pass

    def test_g_2(self):
        self.assertEquals(funcs.g(0, 0), 0)
        pass

    def test_hypotenuse_1(self):
        self.assertEquals(funcs.hypotenuse(3, 4), 5)
        pass

    def test_hypotenuse_2(self):
        self.assertEquals(funcs.hypotenuse(5, 12), 13)
        pass

    def test_isPositive_1(self):
        self.assertEquals(funcs.is_positive(1), True)
        pass

    def test_isPositive_2(self):
        self.assertEquals(funcs.is_positive(-1), False)
        pass

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

