def constructSubmatrix(matrix, delRows, delCols):
    for x in delRows:
        matrix = [i for i in matrix if i is not matrix[x]]
    o = 0
    for y in matrix:
        for z in delCols:
            del y[z-o]
            o += 1
        o = 0
    return matrix

"""
Given a matrix (i.e. an array of arrays), find its submatrix 
obtained by deleting the specified rows and columns.

Example

For

matrix = [[1, 0, 0, 2], 
          [0, 5, 0, 1], 
          [0, 0, 3, 5]]

rowsToDelete = [1], and columnsToDelete = [0, 2], the output should be

constructSubmatrix(matrix, rowsToDelete, columnsToDelete) = [[0, 2],
                                                             [0, 5]]

"""

matrix = [[1, 0, 0, 2], 
          [0, 5, 0, 1], 
          [0, 0, 3, 5]]

delRows = [1]
delCols = [0, 2]
if __name__ == '__main__':
    print(constructSubmatrix(matrix, delRows, delCols))
