class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float("inf") for i in range(amount+1)]
        dp[0] = 0
        for i in range(len(coins)):
            for j in range(amount+1):
                if j >= coins[i]:
                    dp[j] = min(dp[j],1 + dp[j-coins[i]])
        return dp[amount] if dp[amount] != float("inf") else -1

    
s = Solution()
coins = [1,5,6,8]
am = 11
print(s.coinChange(coins,am))