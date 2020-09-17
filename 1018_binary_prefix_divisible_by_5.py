"""
Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i] interpreted as a binary number (from most-significant-bit to least-significant-bit.)

Return a list of booleans answer, where answer[i] is true if and only if N_i is divisible by 5.
"""

def prefixesDivBy5(A):
    ans = []
    value = 0
    for i in range(0, len(A)):
        value <<= 1 # or simply *2
        value += A[i]
        value %= 5
        if value:
            ans.append(False)
        else:
            ans.append(True)
    return ans
print(prefixesDivBy5([0,1,1]))