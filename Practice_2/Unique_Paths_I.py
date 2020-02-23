"""MAIN IDEA --> Appraoch is really simple. 1st row will be all ones because there is only
one way to reach all the cells in first row. Similarly 1st column will also
be all ones because there is only one way to reach all the cells in first
colmn. After that starting from index (1,1) we calculate each cells value as
sum of previous cell and upper cell and reach the last cell.
return the value of last cell"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = [[0 for i in range(m)]for i in range(n)]

        """------------------ Make 1st row zero ----------------------"""
        for i in range(m):
            grid[0][i] = 1
        """------------------ Make 1st column zero -------------------"""
        for i in range(n):
            grid[i][0] = 1
        
        """------------------ Dynamic Programming (Bottom-Up)------------------"""
        for i in range(1,n):
            for j in range(1,m):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[n-1][m-1]


s = Solution()
print(s.uniquePaths(7,3))