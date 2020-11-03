"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

>>> searchPosition([1, 3, 5, 6], 5)
2

>>> searchPosition([1, 3, 5, 6], 2)
1

>>> searchPosition([1, 3, 5, 6], 7)
4

>>> searchPosition([1, 3, 5, 6], 0)
0

>>> searchPosition([1], 0)
0

"""
 
def searchPosition(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums.sort() 
        return nums.index(target)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')