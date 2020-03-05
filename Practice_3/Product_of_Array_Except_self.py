class Solution(object):
    """
    Create 2 arrays left and right where left[i] denotes product of all elements before index i
    right[i] --> Product of all elements after index i
    then for the final result, just iterate overthe original array and for each position in the output array
    do left[i] * right[i]
    """
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        """--------------------- Preprocessing Generate left and right array ---------------------------"""
        left = [1] * n
        right = [1] * n
        left[0] = 1             # product of all element before index 0 = 1 (Since there are no elements before index 0)
        for i in range(1,n):
            left[i] = nums[i-1] * left[i-1]

        right[n-1] = 1             # product of all element after last index = 1 (Since there are no elements after last index)
        for i in range(n-2,-1,-1):
            right[i] = nums[i+1] * right[i+1]
        
        """--------------------- Generate final output array ---------------------------"""
        output = [1]*n
        for i in range(n):
            output[i] = left[i] * right[i] 
        return output
    
s = Solution()
print(s.productExceptSelf([1,2,3,4]))
