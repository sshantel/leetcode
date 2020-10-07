"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.


The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".
>>> J = "aA", S = "aAAbbbb"
3

>>> J = "z", S = "ZZ"
0

"""
 
def numJewelsInStones(J , S):
    for letter in S:
        if letter in J:
            count += 1
    return count

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')