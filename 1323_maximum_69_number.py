"""
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
>>> maximum69Number(9669)
9969
>>> maximum69Number(9996)
9999
>>> maximum69Number(9999)
9999
""" 


def maximum69Number(num):
    l = list(str(num))
    for i,x in enumerate(l):
        if x=='6':
            l[i]='9'
            break
    return int(''.join(l))

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")