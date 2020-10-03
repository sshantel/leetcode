"""

Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.


"""
 
def numIdenticalPairs(nums):
    count = 0
    for i, element in enumerate(nums): 
        for j, element in enumerate(nums):
            if nums[i] == nums[j] and i < j:
                count += 1
    return count
print(numIdenticalPairs([1,2,3,1,1,3]))
print(numIdenticalPairs([1,1,1,1]))
print(numIdenticalPairs([1,2,3]))