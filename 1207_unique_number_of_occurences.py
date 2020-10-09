"""
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

>>> uniqueOccurrences([1,2,2,1,1,3])
True

>>> uniqueOccurrences([1,2])
False

>>> uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])
True
"""
 
def uniqueOccurrences(arr):
    arr_dict = {}
    for number in arr:
        if number not in arr_dict:
            arr_dict[number] = 1
        else:
            arr_dict[number] += 1  
    set_occur = set() 
    for count in arr_dict.values():
        if count in set_occur:
            return False
        else:
            set_occur.add(count)
    return True

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')