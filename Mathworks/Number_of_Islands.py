"""MAIN IDEA --> Scan the grid from left to right and run a DFS whenever you encounter a 1. 
The DFS will terminate when it will traverse one connected component(bunch of connected ones !)
The again while traversing the grid, whenever we encounter a 1, we start a DFS and that 
DFS will end when it completes traversing another connected component(island)
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        no_of_islands = 0
        nr = len(grid)
        nc = len(grid[0])
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1:
                    no_of_islands += 1
                    self.DFS(grid,r,c)
        return no_of_islands
    
    def DFS(self,grid,r,c):
        nr = len(grid)
        nc = len(grid[0]) 
        if r < 0 or r > nr-1 or c < 0 or c > nc-1 or grid[r][c] == 'V' or grid[r][c] == 0:
            return
        
        grid[r][c] = 'V'
        self.DFS(grid,r+1,c)
        self.DFS(grid,r-1,c)
        self.DFS(grid,r,c+1)
        self.DFS(grid,r,c-1)

grid = [[1,1,0,0,0]
        ,[1,1,0,0,0]
        ,[0,0,1,0,0]
        ,[0,0,0,1,1]]

s = Solution()
print(s.numIslands(grid))