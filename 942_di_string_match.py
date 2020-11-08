"""
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]
 

>>> diStringMatch("IDID")
[0, 4, 1, 3, 2]

>>> diStringMatch("III")
[0, 1, 2, 3]

>>> diStringMatch("DDI")
[3, 2, 0, 1]

"""

 
def diStringMatch(S):
    mx = len(S)
    mi = 0
    r = [] 
     
    for c in S:
        if c == 'I':
            r.append(mi)
            mi += 1
        else:
            r.append(mx)
            mx -= 1
    r.append(mx)
    return r

if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")