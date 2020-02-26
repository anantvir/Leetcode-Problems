from collections import Counter
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c = Counter(nums)
        res = 0
        for key in c:
            if k > 0 and key + k in c or k == 0 and c[key] > 1:
                res += 1
        return res

nums = [3, 1, 4, 1, 5] 
k = 2
s = Solution()
s.findPairs(nums,k)
        