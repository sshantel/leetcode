"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
"""

def isPalindrome(s):
    result_list = s.lower().strip().split() 
    result = "".join(result_list)
    res = re.sub(r'[^\w\s]', '', result) 
    print(res)
    return res[::-1] == res