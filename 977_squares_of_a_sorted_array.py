"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
"""
 
def sortedSquares(A):
    list = []
    for num in A:
        num = num * num
        list.append(num)
    return sorted(list)
print(sortedSquares([-4, -1, 0, 3, 10]))
print(sortedSquares([-7, -3, 2, 3, 11]))
