"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?




"""
from typing import List 

def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """  
    k = k % len(nums)
    answer = nums[-k:] + nums[:-k] 
    for i in range(len(nums)):
        nums[i] = answer[i]
    return nums

print(rotate([1,2,3,4,5,6,7], 3))