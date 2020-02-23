class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        nr = len(obstacleGrid)
        nc = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        """---------------- Initialize first row -------------------"""
        # if cell contains 0 then updtae cells value to be value of previous cell. Because number of ways to reach this cell depend on previous cell
        for i in range(1,nc):
            if obstacleGrid[0][i] == 0:
                obstacleGrid[0][i] = obstacleGrid[0][i-1]
            else:
                obstacleGrid[0][i] = 0
        """----------------- Initialize first column -------------------"""
        # if cell contains 0 then updtae cells value to be value of previous cell. Because number of ways to reach this cell depend on previous cell
        for i in range(1,nr):
            if obstacleGrid[i][0] == 0:
                obstacleGrid[i][0] = obstacleGrid[i-1][0]
            else:
                obstacleGrid[i][0] = 0
        
        for r in range(1,nr):
            for c in range(1,nc):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                else:
                    obstacleGrid[r][c] = obstacleGrid[r-1][c] + obstacleGrid[r][c-1]
        return obstacleGrid[nr-1][nc-1]


grid =  [[0,0,0],
        [0,1,0],
        [0,0,0]]
s = Solution()
print(s.uniquePathsWithObstacles(grid))
        