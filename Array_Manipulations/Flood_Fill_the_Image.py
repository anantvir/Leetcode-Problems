from collections import deque
class Solution(object):

    """------------------------------------------- Classic BFS Question ------------------------------------------"""
    def floodFill(self, grid, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if not grid:
            return []
        if newColor == grid[sr][sc]:
            return grid
        strt_pixel_clr = grid[sr][sc]
        Q = deque()
        Q.append((sr,sc,strt_pixel_clr))
        nr = len(grid)
        nc = len(grid[0])
        while Q:
            curr_r,curr_c,curr_clr = Q.popleft()
            grid[curr_r][curr_c] = newColor
            #grid[curr_r][curr_c] = 'V'
            for nbr in [(curr_r+1,curr_c),(curr_r-1,curr_c),(curr_r,curr_c+1),(curr_r,curr_c-1)]:
                nbr_r = nbr[0]
                nbr_c = nbr[1]
                if 0 <= nbr_r <= nr-1 and 0 <= nbr_c <= nc-1 and grid[nbr_r][nbr_c] == strt_pixel_clr:
                    Q.append((nbr_r,nbr_c,grid[nbr_r][nbr_c]))
        return grid
    
image = [[0,0,0],[0,1,1]]
sr = 1
sc = 1
newColor = 1

s = Solution()
print(s.floodFill(image,sr,sc,newColor))
