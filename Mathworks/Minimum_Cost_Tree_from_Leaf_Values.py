class Solution(object):

    """--------------- Same DP approach as matrix chain multiplication -----------------------"""
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        """------------------ Create Table for Bottom Up DP--------------------------"""
        m = [[float("inf") for i in range(n)] for i in range(n)]

        """----------------- Preprocessing(elements at diagnol = 0)----------------------"""
        # Since there is no cost of merging one node
        for i in range(n):
            m[i][i] = 0

        for l in range(2,n+1):
            for i in range(n-l+1):
                j = i+l-1
                for k in range(i,j):
                    cost = m[i][k] + m[k+1][j] + max(arr[i:k+1]) * max(arr[k+1:j+1])
                    if cost < m[i][j]:
                        m[i][j] = cost
        return m[0][-1]


s = Solution()
print(s.mctFromLeafValues([6,2,4,5]))