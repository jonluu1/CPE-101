import unittest
import loops

class TestLoops(unittest.TestCase):
   def test_for(self):
      self.assertEqual(loops.for_version([1,2,3]), [3,2,1])

   def test_while(self):
      self.assertEqual(loops.while_version([1,2,3]), [3,2,1])

if __name__ == '__main__':
   unittest.main()

