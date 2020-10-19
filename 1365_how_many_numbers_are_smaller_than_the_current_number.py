"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

>>> smallerNumbersThanCurrent([8,1,2,2,3])
[4, 0, 1, 1, 3]

>>> smallerNumbersThanCurrent([6,5,4,8])
[2, 1, 0, 3]

>>> smallerNumbersThanCurrent([7,7,7,7])
[0, 0, 0, 0]

"""
 
def smallerNumbersThanCurrent(nums):
    
    number_of_smaller = [] 
    for i in range(len(nums)):
        count = 0 
        for j in range(len(nums)):
            if nums[i] > nums[j] and j != i:
                count += 1 
        number_of_smaller.append(count)
                
    return number_of_smaller

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")