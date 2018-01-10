#
# Test cases example for lab 1.
#

import unittest      # import the module that supports writing unit tests

# Define a class that will be used for these test cases.
# This class will include testing functions.
#
# Much of this code should be viewed as boilerplate for now.
#
class TestsLab1(unittest.TestCase):
   def test_expressions(self):         # Defines one testing function.
      self.assertEqual(0 + 1, 1)
      self.assertEqual(2 * 2, 4)
      self.assertEqual(19 // 3, 6)
      self.assertEqual(19 / 3, 6)
      self.assertAlmostEqual(19 / 3.0, 6.3333333)
      self.assertAlmostEqual(19.0 / 3.0, 6.3333333)
      self.assertEqual(4 * 2 + 27 // 3 + 4, 21)
      self.assertEqual(4 * (2 + 27) // 3 + 4, 42)
      # Add code here (like the line above) for the additional test cases.


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

