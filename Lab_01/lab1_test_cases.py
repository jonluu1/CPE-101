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
      # Add code here (like the line above) for the additional test cases.


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

