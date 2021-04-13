"""
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
"""
from collections import defaultdict
from math import inf
def minimum_window_substring(s, t):
  seen = {}
  for char in t:
    if char in seen:
      seen[char] += 1
    else:
      seen[char] = 1
  left = 0
  result = [0, inf]
  remaing_char = len(t)
   
  for right, right_elem in enumerate(s):
    if right_elem in seen:
      seen[right_elem] -= 1   
      if seen[right_elem] >= 0:
        remaing_char -= 1
     
    while remaing_char == 0:
      if (result[1]-result[0]) > (right-left):
        result[0] = left
        result[1] = right
        
      if s[left] in seen:
        seen[s[left]] += 1
        if seen[s[left]] > 0: 
          remaing_char += 1
          
      left += 1
          
  if result[1] == inf:
    return ""
  else:
    return s[result[0]: result[1]+1]
    
s = "ADOBECODEBANC"
t = "ABC"
print(minimum_window_substring(s, t))


  


        