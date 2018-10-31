def sudoku(grid):
    s, s2, s3 = set(), set(), set()
    # Check Row
    for r in grid:
        if len(set(r)) != 9: return False
    # Check Column
    for c in zip(*grid):
        if len(set(c)) != 9: return False
    # Check 3x3 Spaces
    for x in range(9):
        for j in range(9):
            if j < 3:
                s.add(grid[x][j])
            if j < 6 and j > 2:
                s2.add(grid[x][j])
            if j > 5:
                s3.add(grid[x][j])
            if (x == 2 and j == 8) or (x == 5 and j == 8):
                if len(s) != 9 or len(s2) != 9 or len(s3) != 9:
                    return False
                s.clear(), s2.clear(), s3.clear()
    return True

"""
Sudoku is a number-placement puzzle. The objective is to fill 
a 9 × 9 grid with digits so that each column, each row, and 
each of the nine 3 × 3 sub-grids that compose the grid contains 
all of the digits from 1 to 9. This algorithm should check if the 
given grid of numbers represents a correct solution to Sudoku.

Example:
For the first example below, the output should be true. 
For the other grid, the output should be false: each of 
the nine 3 × 3 sub-grids should contain all of the digits from 1 to 9.
"""

grid = [
 [1,3,2,5,4,6,9,8,7], 
 [4,6,5,8,7,9,3,2,1], 
 [7,9,8,2,1,3,6,5,4], 
 [9,2,1,4,3,5,8,7,6], 
 [3,5,4,7,6,8,2,1,9], 
 [6,8,7,1,9,2,5,4,3], 
 [5,7,6,9,8,1,4,3,2], 
 [2,4,3,6,5,7,1,9,8], 
 [8,1,9,3,2,4,7,6,5]]
if __name__ == '__main__':
    print(sudoku(grid))
