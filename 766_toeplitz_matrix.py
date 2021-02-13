"""
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
>>> isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])
True
>>> isToeplitzMatrix([[1,2],[2,2]])
False


"""
 
def isToeplitzMatrix(matrix): 
        
    row = len(matrix) - 1
    column = len(matrix[0]) - 1
    for i in range(row): 
        for j in range(column): 
            if matrix[i][j] != matrix[i+1][j+1]:
                return False
    return True

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')