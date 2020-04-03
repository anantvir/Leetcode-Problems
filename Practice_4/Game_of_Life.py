import copy

"""
MAIN IDEA --> Just traverse the grid and apply the rules. But keep in mind that we cannot modify the grid in place without making a copy of the grid. Because
if we do, then we will use modified grid for the next operations. So make a copy of the grid. Check the elements from this copied grid before applying the rules.
Apply the rules in the actual grid and keep the copy unchanged !
"""

class Solution(object):
    def gameOfLife(self, grid):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not grid:
            return []
        
        grid_copy = copy.deepcopy(grid)
        nr = len(grid)
        nc = len(grid[0])
        for r in range(nr):
            for c in range(nc):
                """------------------------ Handle dead cells (Rule 4) ----------------------------"""
                if grid_copy[r][c] == 0:
                    live_count = 0
                    for nbr in [(r+1,c),(r-1,c),(r,c+1),(r,c-1),(r+1,c+1),(r-1,c+1),(r-1,c-1),(r+1,c-1)]:
                        new_r = nbr[0]
                        new_c = nbr[1]
                        if new_r >= 0 and new_r <= nr-1 and new_c >= 0 and new_c <= nc-1:
                            if grid_copy[new_r][new_c] == 1:
                                live_count += 1
                    if live_count == 3:
                        grid[r][c] = 1
                """----------------------- Handle live cells (Rule 1,2,3) -----------------------------"""
                if grid_copy[r][c] == 1:
                    live_count = 0
                    for nbr in [(r+1,c),(r-1,c),(r,c+1),(r,c-1),(r+1,c+1),(r-1,c+1),(r-1,c-1),(r+1,c-1)]:
                        new_r = nbr[0]
                        new_c = nbr[1]
                        if new_r >= 0 and new_r <= nr-1 and new_c >= 0 and new_c <= nc-1:
                            if grid_copy[new_r][new_c] == 1:
                                live_count += 1
                    if live_count < 2 or live_count > 3:
                        grid[r][c] = 0
                        

grid = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
s = Solution()
print(s.gameOfLife(grid))
print(grid)