"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

>>> replaceElements([17,18,5,4,6,1])
[18, 6, 6, 6, 1, -1]

"""

def replaceElements(arr): 
    output = [-1]
    current_max = arr[-1]
    for index in range(len(arr)-1,-1, -1):
        if arr[index] > current_max:
            current_max = arr[index]
        output.append(current_max)
    output.pop()
    return output[::-1]

if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")

