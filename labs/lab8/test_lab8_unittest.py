import unittest
from lab8 import count_letters, reverse_string, is_palindrome, match_ends, front_x, sort_last

class Testlab8(unittest.TestCase):
    def setUp(self):
        pass

    def test_letters(self):
        self.assertEqual( count_letters('banana', 'n'), 2)
        self.assertEqual( count_letters('banana', 'o'), 0)

    def test_reverse(self):
        self.assertEqual( reverse_string('hello'), 'olleh')
        self.assertEqual( reverse_string('abba'), 'abba')

    def test_palindrome(self):
        self.assertEqual( is_palindrome('abba'), True)
        self.assertEqual( is_palindrome('hello'), False)

    def test_match_ends(self):
        self.assertEqual( match_ends(['racecar', 'war', 'r', 'staples']), 2)
        self.assertEqual( match_ends(['war', 'r', 'apple']), 0)
        self.assertEqual( match_ends([]), 0)

    def test_front_x(self):
        self.assertEqual( front_x(['mix',' xyz', 'apple', 'xanadu', 'aardvark']), ['xanadu', 'xyz', 'apple', 'mix'])

    def test_sort_last(self):
        self.assertEqual( sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [(1, 7), (1, 3), (3, 4, 5), (2, 2)])

if __name__ == '__main__':
        unittest.main()


