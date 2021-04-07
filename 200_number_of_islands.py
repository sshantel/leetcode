"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""
def numIslands(grid):
  m = len(grid)
  n = len(grid[0])

  def dfs(i, j):
    grid[i][j] = "0"
    directions = [(i+1,j), (i-1,j), (i, j+1), (i, j-1)]
    for dir_row, dir_col in directions:
      if 0<= dir_row<m and 0<=dir_col<n and grid[dir_row][dir_col] == '1':
        dfs(dir_row, dir_col)

  count = 0
  for i in range(m):
    for j in range(n):
      if grid[i][j] == "1":
        count += 1
        dfs(i, j)

  return count

print(numIslands((["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"])))