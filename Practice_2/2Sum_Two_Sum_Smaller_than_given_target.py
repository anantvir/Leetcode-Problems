"""In a given list find number of pairs such that sum of pairs is less than the given target"""
class Solution:
    def TwoSum(self,nums,target):
        nums.sort()
        i = 0
        j = len(nums) - 1
        pairs = 0
        while i < j:
            if nums[i] + nums[j] >= target:
                j = j - 1
            else:
                pairs = pairs + (j-i)
                i = i + 1
        return pairs


nums = [12,8,3,7,9,4]
s = Solution()
print(s.TwoSum(nums,15))
        