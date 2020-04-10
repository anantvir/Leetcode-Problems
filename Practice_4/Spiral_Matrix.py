class Solution(object):
    def spiralOrder(self, grid):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not grid:
            return []
        nr = len(grid)
        nc = len(grid[0])
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        r = c = 0
        idx = 0         # Intial index in dirs array
        res = []
        for _ in range(nr*nc):
            res.append(grid[r][c])
            grid[r][c] = 'V'
            new_r = r + dirs[idx][0]
            new_c = c + dirs[idx][1]
            if 0 <= new_r <= nr-1 and 0 <= new_c <= nc-1 and grid[new_r][new_c] != 'V':
                r = new_r
                c = new_c
            else:
                """-------------Change Direction -------------------"""
                idx = (idx + 1) % 4         # WHen idx = 4 i.e it will surpass last element of dirs array, idx will be reset to 0
                r = r + dirs[idx][0]
                c = c + dirs[idx][1]
        return res

s = Solution()
grid = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
print(s.spiralOrder(grid))