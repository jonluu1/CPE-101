import unittest
import line

class LineTests(unittest.TestCase):
    def test_line(self):
        testLine = line.Line(0, 0, 1, 1)
        self.assertEquals(testLine.x1, 0)
        self.assertEquals(testLine.y1, 0)
        self.assertEquals(testLine.x2, 1)
        self.assertEquals(testLine.y2, 1)
      # Add code here.
      # 1) Create a Line with x1, y1, x2, y2 values of your choice.
      # 2) Use assertEqual on each field in the new Line to verify
      #    that it holds the expected value.




# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

