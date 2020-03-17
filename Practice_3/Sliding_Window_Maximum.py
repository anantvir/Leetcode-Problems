class Solution(object):
    """------------------------------------ Brute Force -----------------------------------------"""
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        global_max = []
        n = len(nums)
        for i in range(n-k+1):
            curr_max = float("-inf")
            for j in range(i,i+k):
                curr_max = max(curr_max,nums[j])
            global_max.append(curr_max)
        return global_max

s = Solution()
nums = [1,-1]
k = 1
print(s.maxSlidingWindow(nums,k))

        