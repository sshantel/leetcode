"""
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

""" 
from typing import List
def plusOne(digits: List[int]) -> List[int]:
    if digits[-1] < 9:
        digits[-1] += 1
        return digits 
    elif digits[-1] == 9:
        i = -1
        while digits[i] == 9:
            digits[i] = 0
            try:
                if digits[i - 1] < 9:
                    digits[i - 1] += 1
                else:
                    i -= 1
            except: return [1] + digits
        return digits
    else: raise ValueError
print(plusOne([9,9,9]))
print(plusOne([8,9,9]))