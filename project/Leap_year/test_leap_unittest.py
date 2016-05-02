import unittest
from leap_year import is_leap_year

class Testleap(unittest.TestCase):

    def setUp(self):
        pass

    def test_year_1900(self):
        self.assertFalse( is_leap_year(1900))

    def test_year_2000(self):
        self.assertTrue( is_leap_year(2000))

    def test_year_2004(self):
        self.assertTrue( is_leap_year(2004))

    def test_year_2001(self):
        self.assertFalse( is_leap_year(2001))

if __name__ == '__main__':
    unittest.main()