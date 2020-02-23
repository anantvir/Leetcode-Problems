class Solution(object):

    """--------------- Brute Force Time Limit Exceeded O(n^3)-----------------"""
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        for i in range(n-3+1):
            for j in range(i+1,n-2+1):
                for k in range(j+1,n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        srt_lst = sorted((nums[i],nums[j],nums[k]))
                        if srt_lst not in res:
                            res.append(srt_lst)
        return res

    """------------------ Efficient O(n^2)--------------------------"""
    def threeSum_Optimized(self,nums):
        nums.sort()
        res = []
        for k in range(len(nums)):
            if nums[k] > 0:
                break 
            first = nums[k]
            target = 0 - first
            i = k+1
            j = len(nums)-1
            while i < j:
                if nums[i] + nums[j] > target:
                    if nums[j-1] == nums[j]:
                        while i < j and nums[j-1] == nums[j]:
                            j = j - 1
                    else:
                        j = j - 1
                elif nums[i] + nums[j] < target:
                    if nums[i+1] == nums[i]:
                        while i < j and nums[i+1] == nums[i]:
                            i = i + 1
                    else:
                        i = i + 1
                else:
                    final = sorted([first,nums[i],nums[j]])
                    if final not in res:
                        res.append(final)
                    i = i + 1
                    j = j - 1
        return res


nums = [-2,-3,0,0,-2]

s = Solution()
print(s.threeSum_Optimized(nums))    