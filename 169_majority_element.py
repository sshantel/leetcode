"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

"""

def majorityElement(nums):
    dict = {}

    for element in nums:
        print(f'element is {element}')
        dict[element] = dict.get(element, 0) + 1
        print(f'dict is {dict}')

    for key, value in dict.items():
        print(f'key is {key}')
        print(f'value is {value}')
        if value > len(nums) / 2:
            return key

    return -1 

print(majorityElement([3,2]))