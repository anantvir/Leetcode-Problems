class Solution(object):

    """-------------------------------- Recursive Traversal of Island in the grid ------------------------------"""
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nr = len(grid)
        nc = len(grid[0])
        # Start scanning the grid row by row left to right
        res = []
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1:
                    count = self.DFS(grid,r,c)
                    res.append(count)
        if res:
            return max(res)
        else:
            return 0
    
    def DFS(self,grid,r,c):
        nr = len(grid)
        nc = len(grid[0])
        if r < 0 or r > nr-1 or c < 0 or c > nc-1 or grid[r][c] == 'V' or grid[r][c] == 0:
            return 0
        grid[r][c] = 'V'
        return 1 + self.DFS(grid,r+1,c) + self.DFS(grid,r-1,c) + self.DFS(grid,r,c+1) + self.DFS(grid,r,c-1)
    
    """------------------------------ Iterative Approach for each island in the grid--------------------------------"""
    def maxAreaOfIsland_Iterative(self,grid):
        nr = len(grid)
        nc = len(grid[0])
        global_max = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1:
                    size = 0
                    stack = []
                    stack.append((r,c))
                    grid[r][c] = 'V'
                    while stack:
                        curr_r,curr_c = stack.pop()
                        size += 1
                        for neighbour in [(curr_r+1,curr_c),(curr_r-1,curr_c),(curr_r,curr_c+1),(curr_r,curr_c-1)]:
                            nb_r = neighbour[0]
                            nb_c = neighbour[1]
                            if 0 <= nb_r <= nr-1 and 0 <= nb_c <= nc-1:
                                if grid[nb_r][nb_c] != 'V' and grid[nb_r][nb_c] != 0:
                                    grid[nb_r][nb_c] = 'V'
                                    stack.append((nb_r,nb_c))
                    global_max = max(size,global_max)
        return global_max



grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
grid2 = [[0,0,0,0,0,0,0,0]]
s = Solution()
print(s.maxAreaOfIsland_Iterative(grid)) 
        