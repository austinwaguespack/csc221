def is_leap_year(year):
    '''
    >>> is_leap_year(1900)
    False
    >>> is_leap_year(2000)
    True
    >>> is_leap_year(2004)
    True
    '''
    year = int(year)
    if year%4== 0 and year%400 == 0 and year%100 ==0:
        return True
    elif year%4==0 and year%100==0:
        return False
    elif year%4==0:
        return True
    elif year:
        return False
