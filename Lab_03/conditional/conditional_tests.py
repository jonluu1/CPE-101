import unittest
import conditional


class TestCases(unittest.TestCase):
    def test_case_1(self):
        n1 = 10
        n2 = 11
        self.assertEqual(conditional.max_101(n1, n2), 11)

    def test_case_2(self):
        n1 = 11
        n2 = 10
        self.assertEqual(conditional.max_101(n1, n2), 11)

    def test_case_3(self):
        n1 = 1.1
        n2 = 1.0
        n3 = 0.9
        self.assertEqual(conditional.max_of_three(n1, n2, n3), 1.1)

    def test_case_4(self):
        n1 = 1.0
        n2 = 1.1
        n3 = 0.9
        self.assertEqual(conditional.max_of_three(n1, n2, n3), 1.1)

    def test_case_5(self):
        n1 = 1.0
        n2 = 0.9
        n3 = 1.1
        self.assertEqual(conditional.max_of_three(n1, n2, n3), 1.1)

    def test_case_6(self):
        day = 0
        self.assertEqual(conditional.rental_late_fee(day), 0)

    def test_case_7(self):
        day = 5
        self.assertEqual(conditional.rental_late_fee(day), 5)

    def test_case_8(self):
        day = 11
        self.assertEqual(conditional.rental_late_fee(day), 7)

    def test_case_9(self):
        day = 20
        self.assertEqual(conditional.rental_late_fee(day), 19)

    def test_case_10(self):
        day = 25
        self.assertEqual(conditional.rental_late_fee(day), 100)


# Run the unit tests.

if __name__ == '__main__':
    unittest.main()