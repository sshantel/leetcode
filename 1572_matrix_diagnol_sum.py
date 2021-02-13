"""

Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

>>> diagonalSum([[1,2,3],[4,5,6],[7,8,9]])
25
>>> diagonalSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]])
8
>>> diagonalSum([[5]])
5
"""

def diagonalSum(max):
    principal = 0
    secondary = 0
    for i in range(0, len(max)):  
        for j in range(0, len(max)):  

            # Condition for principal diagonal 
            if (i == j): 
                principal += max[i][j] 

            # Condition for secondary diagonal 
            elif ((i + j) == (len(max) - 1)): 
                secondary += max[i][j] 

    return principal + secondary

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')