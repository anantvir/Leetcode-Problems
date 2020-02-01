"""Idea is to create all possible shapes starting at that index where we encounter 1st one in the grid !
Example [(0, 0), (0, 1), (1, 1)] is one shape. We find all such shapes of all the islands and keep
adding them to a set. Set will not store duplicates so the same shapes will not be repeated
"""


class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        shapes = set()
        rows = len(grid)
        cols = len(grid[0])
        def DFS(r,c,r0,c0):
            """If r and c are in grid boundary and the cell is not visited already or if its not zero then enter"""
            if  r >=0 and r <= rows-1 and c >= 0 and c <= cols-1 and grid[r][c] != 'V' and grid[r][c] != 0:
                shape.add((r-r0,c-c0))      # Get shape of current cell wrt base coordinates r0 and c0
                grid[r][c] = 'V'
                DFS(r+1,c,r0,c0)
                DFS(r-1,c,r0,c0)
                DFS(r,c+1,r0,c0)
                DFS(r,c-1,r0,c0)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:         # If we encounter a 1, run DFS
                    shape = set()           # To store the shape of island starting at current 1 we encountered
                    DFS(r,c,r,c)
                    if shape:
                        """--------- IMPORTANT --> We add frozen set in shapes set because regular set
                        is not hashable because its mutable. Frozenset is immutable, so we add it because
                        its hash value will not change in future"""
                        shapes.add(frozenset(shape))    
        return len(shapes)                  # Shapes contains all possible unique shapes of the islands,so its length will return the total number of unique islands !

g = [[1,1,0,1,1],
    [1,0,0,0,0],
    [0,0,0,0,1],
    [1,1,0,1,1]]
s = Solution()
print(s.numDistinctIslands(g))
