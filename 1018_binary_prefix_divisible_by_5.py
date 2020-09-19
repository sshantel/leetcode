"""
Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i] interpreted as a binary number (from most-significant-bit to least-significant-bit.)

Return a list of booleans answer, where answer[i] is true if and only if N_i is divisible by 5.
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