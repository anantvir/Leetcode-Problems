"""Idea is to find all posbbile combinations where we can place the buildings by using itertools.combinations from
python, for each combination run a BFS and record the maximum distance of any node. For all the combinations choose the
minimu of such maximum distances calculated"""

from itertools import combinations
from collections import deque
class Solution:
    def Office_Building(self,w,h,n):
        list_of_cells = [i for i in range(w*h)]                 # Flatten the grid into 1D array with numbers from 0,1,2....n-1
        global_min_dist = float("inf")
        for combination in combinations(list_of_cells,n):       # Get all combinations example (3,6,3),(6,7,8)...
            grid = [[-1 for i in range(h)]for i in range(w)]    # For each combination, create a new grid and queue
            Q = deque()
            nr = len(grid)
            nc = len(grid[0])
            for p in combination:
                r = p // h                                      # Calculate r,c in grid from each element of combination tuple
                c = p % h
                grid[r][c] = 0                                  # Mark those combinations as potential building spots i.e 0 and append to the queue
                Q.append((r,c,0))
            max_dist = -1                                       # For every combination, we calculate the max_dist
            """------------------------------- BFS ---------------------------------------------"""
            while Q:
                curr_r,curr_c,curr_d = Q.popleft()
                max_dist = max(max_dist,curr_d)
                for nbr in [(curr_r+1,curr_c),(curr_r-1,curr_c),(curr_r,curr_c+1),(curr_r,curr_c-1)]:
                    r,c = nbr[0],nbr[1]
                    if 0 <= r <= nr-1 and 0 <= c <= nc-1: 
                        if grid[r][c] != 0 and grid[r][c] == -1:
                            grid[r][c] = curr_d + 1
                            Q.append((r,c,curr_d+1))
            global_min_dist = min(global_min_dist, max_dist)     # Declare this variable in global scope because it needs to be updated for all combinations
        return global_min_dist

s = Solution()
print(s.Office_Building(2,3,2))