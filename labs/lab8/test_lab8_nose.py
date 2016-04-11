import lab8


def test_count_letters():
    assert lab8.count_letters('banana', 'n') == 2
    assert lab8.count_letters('banana', 'o') == 0
    assert lab8.count_letters('banana', 'a') == 3

def test_reverse_String():
    assert lab8.reverse_string('hello') == ('olleh')
    assert lab8.reverse_string('abba') == ('abba')

def test_is_palindrome():
    assert lab8.is_palindrome('abba') == True
    assert lab8.is_palindrome('hello') == False

def test_match_ends():
    assert lab8.match_ends(['racecar', 'war', 'r', 'staples']) == 2
    assert lab8.match_ends([]) == 0

def test_front_x():
    assert lab8.front_x(['mix',' xyz', 'apple', 'xanadu', 'aardvark']) == ['xanadu', 'xyz', 'apple', 'mix']

def test_sort_last():
    assert lab8.sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]) == [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
