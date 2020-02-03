"""----------------- Approach --> BFS ------------------------

Initially append all rotten oranges to a queue. Then start popping from queue and process each neighbour of popped element
In the queue, we append index of r,c,d  where r,c are indices and d = distance from the origin node
"""
from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        def neighbours(r,c):                                    # Returns neighbour of r,c if neighbour is valid i.e lies inside the grid
            neighbours = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            neighbour_list = []
            for neighbour in neighbours:
                if 0 <= neighbour[0] <= rows - 1 and 0 <= neighbour[1] <= cols - 1:     # Check if neighbour lies inside grid
                    neighbour_list.append(neighbour)
            return neighbour_list
 
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c,0))                           # Initially, append all rotten oranges to the queue

        while queue:
            r,c,d = queue.popleft()
            for neighbour in neighbours(r,c):
                nr = neighbour[0]
                nc = neighbour[1]
                if grid[nr][nc] == 1:                  
                    grid[nr][nc] = 2
                    queue.append((nr,nc,d+1))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return d

g = [[2,1,1],
    [1,1,0],
    [0,1,1]]
s = Solution()
print(s.orangesRotting(g))