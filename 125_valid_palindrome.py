"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
"""

def isPalindrome(s):
        output_s = re.sub('[^A-Za-z0-9]+', '', s).lower() 
        return output_s == output_s[::-1]
         