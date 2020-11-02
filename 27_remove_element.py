"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

>>> removeElement([3, 2, 2, 3], 3)
[2, 2]

>>> removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
[0, 1, 3, 0, 4]

"""


def removeElement(nums, val):
    while val in nums:
        nums.remove(val)
    return nums

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")