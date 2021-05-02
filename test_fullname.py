import unittest
import fullname

class TestCase(unittest.TestCase):

    def test_fullname(self):
        result = fullname.full_name("Aaron", "Rafter")
        self.assertEqual("Aaron", result.first)
        self.assertEqual("Rafter", result.last)
    def test_fullname2(self):
        result = fullname.full_name("1100", "2010")
        self.assertEqual("1100", result.first)
        self.assertEqual("2010", result.last)
    def test_fullname3(self):
        result = fullname.full_name("", "")
        self.assertEqual("", result.first)
        self.assertEqual("", result.last)


if __name__ == '__main__':
    unittest.main()
