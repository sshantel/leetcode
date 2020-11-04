"""
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

>>> dominantIndex([3, 6, 1, 0])
1

>>> dominantIndex([1, 2, 3, 4])
-1

"""
def dominantIndex(nums):
    i = 0
    new_nums = []
    largest_number = nums[i]
    for i in range(len(nums)):
        if nums[i] > largest_number:
            largest_number = nums[i]
    for number in nums:
        if number * 2 <= largest_number:
            new_nums.append(number)
    new_nums.append(largest_number) 
    if len(new_nums) == len(nums):
        return nums.index(largest_number)
    else:
        return -1

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')