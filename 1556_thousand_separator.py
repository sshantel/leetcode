"""
Given an integer n, add a dot (".") as the thousands separator and return it in string format.
>>> thousandSeparator(987)
'987'

>>> thousandSeparator(1234)
'1.234'

>>> thousandSeparator(123456789)
'123.456.789'

""" 

def thousandSeparator(n):
    n = str(n)
    n_backwards = n[::-1] 
    new_str = []
    if len(n) < 4:
        return n
    else:
        for i in range(len(n_backwards)):
            if i > 0 and i % 3 == 0:
                new_str.append('.') 
            new_str.append(n_backwards[i])
        return ''.join(new_str[::-1])

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
