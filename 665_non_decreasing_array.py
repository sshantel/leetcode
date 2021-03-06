"""
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).
"""

 
def checkPossibility(nums):
    count = 0
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]: 
            if count<1:
                if i==0:
                    nums[i]=nums[i+1] 
                elif nums[i-1]<=nums[i+1]:
                    nums[i]=nums[i-1]        
                else:
                    nums[i+1]=nums[i]
                count+=1               
            else:
                return False 
    return True    