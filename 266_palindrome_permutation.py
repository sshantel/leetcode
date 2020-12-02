"""
Given a string, determine if a permutation of the string could form a palindrome.
<<< canPermutePalindrome('code')
False

<<< canPermutePalindrome('aab')
True

<<< canPermutePalindrome('carerac')
True

"""


def canPermutePalindrome(s):
    stack = []
    s = list(s)
    while s:
        m = s.pop()
        if m in stack:
            stack.remove(m)
        else:
            stack.append(m)
    return len(stack) <= 1


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n✨ ALL TESTS PASSED!\n")

