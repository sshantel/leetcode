"""
Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

>>> isHappy(19)
True

"""
 
def isHappy(n):
    for i in range(6): 
        result = 0
        for digit in str(n):
            result = result + (int(digit) ** 2)
        n = result
    
    return True if result == 1 else False



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')