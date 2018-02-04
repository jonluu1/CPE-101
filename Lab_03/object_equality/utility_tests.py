import unittest
import utility

class TestCases(unittest.TestCase):
   def test_epsilon_equal_1(self):
      self.assertTrue(utility.epsilon_equal(1, 1))


   def test_epsilon_equal_2(self):
      self.assertTrue(utility.epsilon_equal(1.00000000001, 1))
      self.assertTrue(utility.epsilon_equal(1, 1.00000000001))


   def test_epsilon_equal_3(self):
      self.assertFalse(utility.epsilon_equal(1.1, 1))
      self.assertFalse(utility.epsilon_equal(1, 1.1))


   def test_epsilon_equal_4(self):
      self.assertTrue(utility.epsilon_equal(0.999999999, 1))
      self.assertTrue(utility.epsilon_equal(1, 0.999999999))


   def test_epsilon_equal_5(self):
      self.assertFalse(utility.epsilon_equal(0.999, 1))
      self.assertTrue(utility.epsilon_equal(0.999, 1, 0.01))
      self.assertFalse(utility.epsilon_equal(1, 0.999))
      self.assertTrue(utility.epsilon_equal(1, 0.999, 0.01))


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

