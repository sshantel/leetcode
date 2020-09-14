"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        poop = s.split()
        last_poop = poop[-1]
        print(len(last_poop))
v = Solution()
print(v.lengthOfLastWord('Hello World'))