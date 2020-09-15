"""
Given a string s containing only lower case English letters and the '?' character, convert all the '?' characters into lower case letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.

"""
class Solution:
    def modifyString(self, s: str) -> str:
        lowercase_letters_str = "abcdefghijklmnopqrstuvwxyz"
        # lowercase_letter_array = [letter for letter in lowercase_letters_str]
        lowercase_letter_array = []
        for lwrltr in lowercase_letters_str:
            lowercase_letter_array.append(lwrltr)
        print(lowercase_letter_array)
        modified_string = ''
        # for letter in s:
        #     if letter != '?':
        #         modified_string += letter
        #     else:
        #         modified_string += lwrltr

        return modified_string 
s = Solution()
print(s.modifyString('?zs'))