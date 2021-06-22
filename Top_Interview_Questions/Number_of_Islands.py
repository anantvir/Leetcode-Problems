class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # Scan the 2D grid, whenever we encounter 1, we start a DFS if that node is not already visited
        # and increment the island counter. Total no of islands = Total no. of DFS's initiated

        nr = len(grid)
        nc = len(grid[0])
        islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    islands += 1
                    self.DFS(grid, r, c)
        return islands

    def DFS(self, grid, r, c):
        nr = len(grid)
        nc = len(grid[0])

        # If node has already been visited 'V' or if its a '0', then backtrack
        if r < 0 or c < 0 or r >= nr or c >= nc or grid[r][c] == 'V' or grid[r][c] == '0':
            return
        grid[r][c] = 'V'
        self.DFS(grid, r+1, c)
        self.DFS(grid, r, c+1)
        self.DFS(grid, r-1, c)
        self.DFS(grid, r, c-1)
