import unittest
import cubevol

class TestCase(unittest.TestCase):
    
    def test_cubevol(self):
        result = cubevol.volume(3, 3, 3)
        self.assertEqual(result, 27)
    def test_cubevol2(self):
        result = cubevol.volume(3, 3, 0)
        self.assertEqual(result, 1)
    def test_cubevol3(self):
        result = cubevol.volume("this", "should", "error")
        self.assertEqual(result, 1)




if __name__ == '__main__':
    unittest.main()
