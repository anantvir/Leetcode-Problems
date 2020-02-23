class Solution(object):

    """----------------------- Brute Force --------------------------"""
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        S = -1
        for i in range(len(A)-1):
            for j in range(i+1,len(A)):
                if A[i]+A[j] < K:
                    S = max(S,A[i]+A[j])
        return S
    
A = [34,23,1,24,75,33,54,8] 
K = 60
s = Solution()
print(s.twoSumLessThanK(A,K))