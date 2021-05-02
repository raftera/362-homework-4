import unittest
import cubevol

class TestCase(unittest.TestCase):
    
    def test_cubevol(self):
        result = cubevol.volume(3, 3, 3)
        self.assertEqual(result, 27)




if __name__ == '__main__':
    unittest.main()
