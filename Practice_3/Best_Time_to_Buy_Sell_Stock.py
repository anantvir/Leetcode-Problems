"""
Main Idea --> Maintain 2 variables, minprice(intially + inf) and maxprofit(intially 0)

Just keep iterating over the array until current element is less than minprice. If current element is not less than min price
then calculate prices[i] - minprice and take the max of this and maxprofit
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = float("inf")
        maxprofit = 0
        n = len(prices)
        for i in range(n):
            if prices[i] < minprice:
                minprice = prices[i]
            else:
                if prices[i] - minprice > maxprofit:
                    maxprofit = prices[i] - minprice
        return maxprofit
        