import unittest
import fullname

class TestCase(unittest.TestCase):

    def test_fullname(self):
        result = fullname.full_name("Aaron", "Rafter")


if __name__ == '__main__':
    unittest.main()
