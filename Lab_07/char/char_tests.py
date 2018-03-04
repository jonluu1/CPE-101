import unittest
import char


class TestChar(unittest.TestCase):
    def test_is_lower_101_1(self):
        string = "a"
        is_lower = char.is_lower_101(string)
        self.assertTrue(is_lower)

    def test_is_lower_101_2(self):
        string = "A"
        is_lower = not char.is_lower_101(string)
        self.assertTrue(is_lower)

    def test_char_rot_13_1(self):
        string = "a"
        rot_13 = char.char_rot_13(string)
        self.assertEqual(rot_13, "n")

    def test_char_rot_13_2(self):
        string = "A"
        rot_13 = char.char_rot_13(string)
        self.assertEqual(rot_13, "N")


if __name__ == '__main__':
    unittest.main()
