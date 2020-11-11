"""
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

>>> threeConsecutiveOdds([2, 6, 4, 1])
False

>>> threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12])
True

""" 


def threeConsecutiveOdds(arr):
    for i in range(len(arr) - 2):
        if arr[i] % 2 == 1:
            if arr[i + 1] % 2 == 1:
                if arr[i + 2] % 2 == 1:
                    return True
    return False
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
