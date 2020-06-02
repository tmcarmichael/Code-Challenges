'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''

def minPathSum(grid):
    assert grid[0], 'Grid is None'
    rows, cols = len(grid), len(grid[0])
    grid = [[sum(grid[0][0:i+1]) for i in range(cols)]] + [[sum(list(zip(*grid))[0][0:j+1]) if h == 0 else grid[j][h] for h in range(cols)] for j in range(1,rows)]
    for i in range(1,rows):
        for j in range(1,cols):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[rows-1][cols-1]
