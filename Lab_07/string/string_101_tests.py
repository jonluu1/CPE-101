import unittest
import string_101


class TestString(unittest.TestCase):
    def test_str_rot_13_1(self):
        string = "ABCDEF"
        rot_13 = string_101.str_rot_13(string)
        self.assertEqual(rot_13, "NOPQRS")

    def test_str_rot_13_2(self):
        string = "abcdef"
        rot_13 = string_101.str_rot_13(string)
        self.assertEqual(rot_13, "nopqrs")

    def test_str_translate_1(self):
        string = "abca"
        old = "a"
        new = "X"
        translate = string_101.str_translate_101(string, old, new)
        self.assertEqual(translate, "XbcX")

    def test_str_translate_2(self):
        string = "ABCX"
        old = "A"
        new = "x"
        translate = string_101.str_translate_101(string, old, new)
        self.assertEqual(translate, "xBCX")


if __name__ == '__main__':
    unittest.main()