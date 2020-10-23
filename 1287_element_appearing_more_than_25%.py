"""
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

Return that integer.
>>> findSpecialInteger([1,2,2,6,6,6,6,7,10])
6

"""


def findSpecialInteger(arr):
    l = len(arr)

    dict_res = {}

    for a in arr:
        if a in dict_res:
            dict_res[a] += 1
        else:
            dict_res[a] = 1
        if dict_res[a] >= (l // 4) + 1:
            return a


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")

