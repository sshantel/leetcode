"""Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.
"""
 
def restoreString(s, indices):
    shuffled_str = [''] * len(s)
    i = 0
    for number in indices:
        shuffled_str[number] = s[i]
        i += 1
    return ''.join(shuffled_str)
    
restoreString("codeleet", [4,5,6,7,0,2,1,3])