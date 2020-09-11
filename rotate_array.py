"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    def rotate(nums, k):
        new_nums_right = []
        new_nums_left = []
        length_nums = len(nums)
        d = (len(nums)) - k 

        new_nums_right.extend(nums[d:]) 
        new_nums_left.extend(nums[:d]) 
        merged_list = []
        merged_list.extend(new_nums_right)
        merged_list.extend(new_nums_left)
        print(merged_list) 

#     rotate([1,2,3,4,5,6,7], 3)
