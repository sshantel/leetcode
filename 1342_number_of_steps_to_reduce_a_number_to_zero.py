"""
Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
>>> numberOfSteps(14)
6
>>> numberOfSteps(8)
4
>>> numberOfSteps(123)
12
"""
 
def numberOfSteps (num):
        count = 0
        while(num != 0):
            if(num % 2 == 0):
                num = num / 2
                count += 1
            else:
                num = num - 1
                count += 1
                 
        return count
if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")