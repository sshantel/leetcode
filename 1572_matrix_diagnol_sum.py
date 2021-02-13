"""

Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

"""

def diagonalSum(max):


    principal = 0
    secondary = 0
    for i in range(0, len(mat)):  
        for j in range(0, len(mat)):  

            # Condition for principal diagonal 
            if (i == j): 
                principal += mat[i][j] 

            # Condition for secondary diagonal 
            elif ((i + j) == (len(mat) - 1)): 
                secondary += mat[i][j] 

    return principal + secondary