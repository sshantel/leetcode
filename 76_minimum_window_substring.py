"""
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
"""

def minWindow(s, t):
    #sliding window approach 
    def create_dict(s, t):
        seen = {}
        for letter in t:
            if letter not in seen:
                seen[letter] = 1
            else:
                seen[letter] += 1
        return seen
    
    def sliding_window(s, t):
        seen = create_dict(s,t) 
        left = 0
        length = []
        length_count = 0
        for right in range(len(s)): 
            if s[right] in seen:   
                seen[s[right]] -= 1 
                if seen[s[right]] < 1:
                    del seen[s[right]] 
            if len(seen) == 0:
                length.append([left, right])
                length_count = right - left + 1 
                left += 1
        return length_count
    return sliding_window(s,t)
print(minWindow("ADOBECODEBANC", "ABC"))
        