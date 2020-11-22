"""

Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

>>> mySqrt(4)
2

>>> mySqrt(8)
2

"""
 
def mySqrt(x):
    y = pow(x, 1/2) 
    return int(y)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')