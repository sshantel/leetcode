"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
<<< addDigits(38)
2

"""
def addDigits(num):
    while num>9:
        res = 0
        for i in str(num):
            res+=int(i)
            num = res
    return num





if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")