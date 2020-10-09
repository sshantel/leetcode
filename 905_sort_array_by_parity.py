"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
You may return any answer array that satisfies this condition.
>>> sortArrayByParity([3,1,2,4])
[2, 4, 3, 1]
>>> sortArrayByParity([1,1,1,4])
[4, 1, 1, 1]

"""
 
def sortArrayByParity(A):
    p = 0
    for i in range(len(A)):
        if A[i] % 2 == 0:
            A[i], A[p] = A[p], A[i]
            p += 1
    return A


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')