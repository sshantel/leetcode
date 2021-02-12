"""
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

"""

 
def transpose(matrix):
    #0,0 => 0, 0
    #0,1 => 1, 0
    #0,2 => 2, 0
#         #flip y, x
#         matrix_grid = [[0] * len(matrix) for row in matrix]
        
    transpose = []
    for i in range(len(matrix[0])):
        row=[]
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        transpose.append(row)
    return transpose