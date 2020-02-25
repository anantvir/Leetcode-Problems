"""Initially set the direction to be dr = 0 and dc = 1, means keep the row same and move the column towards right"""

class Solution(object):
    def spiralOrder(self, grid):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        R = len(grid)
        C = len(grid[0])
        global_list = []
        """dr -> change in row, dc -> change in column"""
        dr = [0,1,0,-1]                 # Order of dr and dc is because we want to move towards right first, then down then left then up
        dc = [1,0,-1,0]
        r = c = di = 0                  # di represents direction(Initially we have 0th direction, means we are moving right in row(dr=0,dc=1))
        for _ in range(R*C):
            global_list.append(grid[r][c])
            grid[r][c] = 'V'
            curr_r = r + dr[di]             # Compute current row and current column
            curr_c = c + dc[di]
            if 0 <= curr_r <= R-1 and 0 <= curr_c <= C-1 and grid[curr_r][curr_c] != 'V':   # check if curr row and col are in counds of the grid and are not already visited
                r = curr_r
                c = curr_c
            else:
                di = (di + 1) % 4               # % 4 because there are 4 elements in dr and dc arrays. this is done to choose direction and reset di when it reaches index 3
                r,c = r + dr[di], c + dc[di]
        return global_list

grid =[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]
s = Solution()
print(s.spiralOrder(grid))
    