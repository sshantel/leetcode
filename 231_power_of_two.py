"""
Given an integer, write a function to determine if it is a power of two.
"""

# import math

# def isPowerOfTwo(n):
#     return n > 0 and math.log2(n) % 1 == 0
# print(isPowerOfTwo(64))

def isPowerOfTwo(n):
    i = 0
    while i < n:
        if n == pow(2, i):
            return True
        i += 1
    return False