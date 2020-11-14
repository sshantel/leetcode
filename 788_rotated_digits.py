"""
X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other (on this case they are rotated in a different direction, in other words 2 or 5 gets mirrored); 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

>>> rotatedDigits(10)
4

"""
 
def rotatedDigits(N):
    count = 0
    for num in range(1, N+1):
        s = str(num) 
        if '3' in s or '4' in s or '7' in s:
            continue
        if '2' in s or '5' in s or '6' in s or '9' in s:
            count += 1
        
    return count


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')