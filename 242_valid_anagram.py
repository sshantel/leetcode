"""
Given two strings s and t , write a function to determine if t is an anagram of s.

<<< isAnagram('anagram', 'nagaram')
True

<<< isAnagram('rat','car')
False

"""


def isAnagram(s, t):
    l1 = list(s)
    l2 = list(t)
    l1.sort()
    l2.sort()
    if l1 == l2:
        return True
    else:
        return False


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n✨ ALL TESTS PASSED!\n")

