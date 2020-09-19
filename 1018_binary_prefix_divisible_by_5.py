"""
Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i] interpreted as a binary number (from most-significant-bit to least-significant-bit.)

Return a list of booleans answer, where answer[i] is true if and only if N_i is divisible by 5.
"""

def prefixesDivBy5(self, A):
    remainder = 0
    answers = len(A) * [None]
    for i in range(len(A)):
        remainder = ((remainder << 1) + A[i]) % 5
        answers[i] = (remainder == 0)
    return answers
