"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.
"""


def search(nums, target: int):
    for index, element in enumerate(nums):
        if nums[index] == target:
            return index
    return -1