class Solution(object):
    """--------------- Brute Force O(n^3) ----------------"""
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = []
        n = len(nums)
        for i in range(n-3+1):
            for j in range(i+1,n-2+1):
                for k in range(j+1,n-1+1):
                    if nums[i] + nums[j] + nums[k] < target:
                        res.append((nums[i],nums[j],nums[k]))
        return res

    """------------------ Efficient O(n^3) ---------------"""
    """MAIN IDEA ---> Select 1 element from nums and run 2 sum smaller on the remaining array. Do this for n-2 elements in the nums array."""
    def ThreeSumSmaller_Optimized(self,nums,target):
        count = 0
        for i in range(len(nums)):
            count = count + self.TwoSumSmaller(nums,i+1,target-nums[i])
        return count
    
    def TwoSumSmaller(self,nums,start_idx,target):            # Finds pairs where sume of 2 elements is smaller than the given target
        nums = nums[start_idx:]
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
    
nums = [1,2,3,5,8]
s = Solution()
print(s.ThreeSumSmaller_Optimized(nums,10))