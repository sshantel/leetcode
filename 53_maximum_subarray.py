"""

"""
 
def maxSubArray(nums):
    if len(nums) == 1: 
        return nums[0]
    elif len(nums) == 0:
        return 0
    else:
        curr_max = nums[0]
        global_max = nums[0]
        for i in range(1, len(nums)):
            if curr_max < 0:
                curr_max = nums[i]
            else:
                curr_max += nums[i]
            if global_max < curr_max:
                global_max = curr_max
        return global_max


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')