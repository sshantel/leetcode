"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

<<< missingNumber([3,0,1])
2

<<< missingNumber([0,1])
2

<<< missingNumber[9,6,4,2,3,5,7,0,1]
8

<<< missingNumber([0])
1

"""

def missingNumber(nums):
    for digit in range(len(nums) + 1 ):
        if digit not in nums:
            return digit


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")