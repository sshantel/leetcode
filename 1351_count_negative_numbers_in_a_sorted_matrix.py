"""
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.
>>> countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])
8
>>> countNegatives([[3,2],[1,0]])
0
>>> countNegatives([1,-1],[-1,-1])
3
>>> countNegatives([[-1]])
1
"""


def countNegatives(grid):
    count = 0
    for number in grid:
        for j in number:
            if j < 0:
                count += 1
    return count

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")