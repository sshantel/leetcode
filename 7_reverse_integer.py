"""Given a 32-bit signed integer, reverse digits of an integer.
 
>>> reverse(123)
321
>>> reverse(-123)
-321
>>> reverse(120)
21

Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""

def reverse(self, x: int) -> int:
    y = str(abs(x))
    y = y.strip()
    y = y[::-1]
    output = int(y)
    
    if output >= 2**31 - 1 or output <= -2**31:
        return 0
    elif x < 0: 
        return -1 * output
    else:
        return output 

if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")