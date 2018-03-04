import unittest
import groups

class TestGroups(unittest.TestCase):

   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)


   # Add tests here

if __name__ == '__main__':
   unittest.main()
