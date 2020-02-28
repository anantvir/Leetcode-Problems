"""
This is a 0/1 Knapsack problem. We want that the sum inside the Knapsack must be equal to sum/2 where sum = total sum of all elements
in the array. We want to choose a subset from the given array whose sum = sum/2
Run a 0/1 knapsack on the entire array and if the last row and last column of the matrix is True, then we have a subset in the
given array whose sum = sum/2.
Example let the given array nums = [1,5,11,5] , n = len(nums), total sum = 22, sum/2 = 11
dp[i][j] is a matrix with n+1 rows where row 0 represents element 0 (although it is not there in nums), we will need it in calculation
dp has dimenions (n+1)*((sum/2)+1) --> Here dimensions will be 5 * 12
dp[i][j] is a boolean value which represents if sum j can be formed by elements from 0 to i. It is True if we can get sum j
else its False.
dp[0][0] = True coz we can get sum  = 0 from element with value 0
dp[i][0] = True because we can get sum = 0 from any element because it doesnt matter what the value of that element is, we just need sum = 0
dp[0][j] = False, because we cannot form any sum j with an element 0 (except dp[0][0])
fill 1st row and 1st column with False except dp[0][0] = True
Then for every starting from i,j = 1,1 to the end of matrix we follow the recursive formula of general Knapsack problem
with a slight modification(because this is a boolean case)
i.e dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]
Since current element will only be considered if current capacity of Knapsack i.e j will be greater than or equal to the current
value in nums, so set the value of dp[i][j] = dp[i-1][j] as the first step inside the 2 for loops(because if the next if condition
if not satisfied, then default value of dp[i][j] should be previous row value)
"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        total_sum = sum(nums)                   # Total sum of entire nums array
        half_sum = total_sum/2                  # What we need in a subset
        if half_sum - int(half_sum) > 0:
            return False
        else:
            half_sum = int(half_sum)

        """---------------Create a 2-D Matrix for Dynamic Programming ------------------"""
        # Dimension will be (n+1)*(half_sum+1), extra row and column because of 0 sum and 0 element to satisfy base cases
        dp = [[False for i in range(half_sum+1)]for i in range(n+1)]

        # Make dp[0][0] = True (Sum of 0 can be formed by element 0)
        dp[0][0] = True

        """----------------- Make 1st Column  = True (0 sum can be formed by any number of elements with any value)-----------------------"""
        for i in range(1,n+1):
            dp[i][0] = True
        """----------------- Make 1st row  = False (j sum cannot be formed by only element 0)-----------------------"""
        for j in range(1,half_sum+1):
            dp[0][j] = False
        
        """------------------ Apply the 0/1 Knapsack for Boolean Case Formula ---------------------"""
        for i in range(1,n+1):
            for j in range(1,half_sum+1):
                dp[i][j] = dp[i-1][j]       # Set it up initially because if the next if condition not satisfied, then access previous row value
                # If sum(current capacity of Knapsack) is greater than or equal to current value in nums(We are deciding if we are choosing the current element from nums in the result pr not)
                if j >= nums[i-1]:   
                    dp[i][j] = dp[i][j] or dp[i-1][j - nums[i-1]]
        return dp[n][half_sum]

nums = [1,2,3,5]
s = Solution()
print(s.canPartition(nums))             
        