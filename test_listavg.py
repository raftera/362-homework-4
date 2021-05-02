import unittest
import listavg

class TestCase(unittest.TestCase):
     def test_listavg(self):
         list = (1, 2, 3)
         result = listavg.average(list)
         self.assertEqual(result, 2)
     def test_listavg2(self):
          list = (0, 0, 0)
          result = listavg.average(list)
          self.assertEqual(result, 0)
     def test_listavg3(self):
          list = (this, should, error)
          result = listavg.average(list)
          self.assertEqual(result, 0)
           


if __name__ == '__main__':
    unittest.main()









