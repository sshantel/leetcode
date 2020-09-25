"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
"""

def firstUniqChar(s):
    dic = {}
    for char in s:
        dic[char] = dic.get(char, 0) + 1
    
    for i, char in enumerate(s): 
        if dic[char] == 1:
            print(dic[char])
            return i
    return -1
print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))s