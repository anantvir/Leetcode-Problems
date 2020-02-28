class Solution(object):
    """
    MAIN IDEA --> Greedy Approach, set curr_sum and global_sum to be = nums[0]. For each element in the nums array, check if that
    element is greater or curr_sum+nums[i] is greater. Whatever is greater, assign that to curr_sum. Then global sum = max(global_sum and curr_sum)
    """
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        curr_sum = nums[0]
        global_sum = nums[0]
        for i in range(1,n):
            curr_sum = max(nums[i],curr_sum + nums[i])
            global_sum = max(global_sum,curr_sum)
        return global_sum

nums = [-1,0,-2]
s = Solution()
print(s.maxSubArray(nums))
        
        