"""

Given a string s, find the length of the longest substring without repeating characters.

#time complexity - linear. O(N)
#space complexity - linear. O(N)
"""


def lengthOfLongestSubstring(s):
    charset = set()
    left = 0
    res = 0
    for right in range(len(s)):
        while s[right] in charset:
            charset.remove(s[left])
            left += 1
        charset.add(s[right])
        # print(f" res is {res}")
        # print(right - left + 1)
        poop = right - left + 1
        if poop > res:
            res = poop
        # res = max(res, right - left + 1)
    return res


print(lengthOfLongestSubstring("abcabcbb"))
