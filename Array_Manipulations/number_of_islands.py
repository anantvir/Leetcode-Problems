"""Scan the grid from left to right. If we encounter a 1, start a DFS search from that node. This DFS will result
in finding 1 island. When we reach a node during DFS, mark it as 0 so that we dont process it twice.
https://www.youtube.com/watch?v=W9F8fDQj7Ok for more details"""

m = [[1,1,0,0,0],
     [1,1,0,0,0],
     [0,0,1,0,0],
     [0,0,0,1,1]]

def ScanGrid(grid):
  if grid == None or len(grid) == 0:
    print('No Grid available !')
  nr = len(grid)
  nc = len(grid[0])
  number_of_islands = 0
  for r in range(nr):
    for c in range(nc):
      if grid[r][c] == 1:               # If we encounter a 1
        number_of_islands += 1          # Increment number of islands
        dfs(grid,r,c)                   # Run a DFS starting from that node
  return number_of_islands

def dfs(grid,r,c):
  nr = len(grid)-1
  nc = len(grid[0])-1

  if r < 0 or c < 0 or r > nr or c > nc or grid[r][c] == 0:         # Check if r and c move out of the grid boundary or if grid[r][c] == 0 which checks if the node has already been visited
    return 

  grid[r][c] = 0      # Setting grid[r][c] = '0' means we have set the node as 'Visited' !
  dfs(grid,r-1,c)       # Check one cell above from current cell
  dfs(grid,r+1,c)       # Check one cell down from current cell
  dfs(grid,r,c-1)       # Check one cell left from current cell
  dfs(grid,r,c+1)       # Check one cell right from current cell

print(ScanGrid(m))