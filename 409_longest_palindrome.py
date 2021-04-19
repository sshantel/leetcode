"""

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

""" 
def longestPalindrome(s):
    ss = set()
    for letter in s:
        if letter not in ss:
            ss.add(letter)
        else:
            ss.remove(letter)
    if len(ss) != 0:
        return len(s) - len(ss) + 1
    else:
        return len(s)