"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
 
def singleNumber(nums) -> int:
    no_duplicate_list = []
    for i in nums:
        if i not in no_duplicate_list:
            no_duplicate_list.append(i)
        else:
            no_duplicate_list.remove(i)
    return no_duplicate_list.pop()
print(singleNumber([2,2,1]))