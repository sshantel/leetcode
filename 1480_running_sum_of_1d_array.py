"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""


class Solution:
    def runningSum(self, nums: int):
        running_nums_total = []
        current = 0
        prev_sum = 0
        for num in nums:
            current = prev_sum + num
            running_nums_total.append(current)
            prev_sum = current
        return running_nums_total


s = Solution()
print(s.runningSum([1, 2, 3, 4]))

