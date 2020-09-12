"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

>>> [1,2,3,1]
True

>>> [1,2,3,4]
False

>>> [1,1,1,3,3,4,3,2,4,2]
True

""" 
from typing import List 

def containsDuplicate(A: List[int]) -> bool:
        S = set()
        
        for elem in A:
            if elem in S:
                return True 
            else:
                S.add(elem)
        return False
print(containsDuplicate([1,2,3,4]))

if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")