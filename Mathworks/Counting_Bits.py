class Solution(object):

    """--------------------- Acceptable O(n*k)-------------------------"""
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        for i in range(num+1):
            ones = self.popcount(i)
            res.append(ones)
        return res

    def popcount(self,x):
        sum = 0
        while x != 0:
            sum += 1
            x = x & x-1                 # If we AND a number n and its previous number n-1, then the least significant bit is flipped and the result becomes smaller and smaller until it becomes zero. So we keep on incrementing the sum
        return sum

    """---------------------------- More Efficient Dynamic Programming O(n) ------------------------------"""
    def countBits_DP(self,num):
        ans = [0]*(num+1)
        i = 0
        b = 1
        ans[0] = 0
        while b <= num:
            while i < b and i + b <= num:
                ans[i + b] = ans[i] + 1
                i += 1
            i = 0
            b <<= 1
        return ans


s = Solution()
print(s.countBits_DP(5))
        