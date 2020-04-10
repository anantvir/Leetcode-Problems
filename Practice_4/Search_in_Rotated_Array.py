"""
MAIN IDEA --> Find pivot element i.e index around which the array has been rotated. Then we can split the array into
2 sorted parts. Then we just need to search the target in one of those 2 sorted arrays
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """------------------- Find pivot by binary search and then search the target by binary search -------------------"""
        def findPivot(start,end,nums):
            mid = (start+end)//2
            if nums[mid] > nums[mid+1]:
                return mid+1            # Found the pivot !
            else:
                if nums[start] > nums[mid]:
                    return findPivot(start,mid-1,nums)
                else:
                    return findPivot(mid+1,end,nums)
        
        def binary_search(start,end,nums,target):
            if start <= end:
                mid = (start+end)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    return binary_search(start,mid-1,nums,target)
                else:
                    return binary_search(mid+1,end,nums,target)
            else:
                return -1
        """----------- If array is already sorted -------------"""
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        if nums[0] < nums[-1]:
            pivot_idx = 0
        else:
            pivot_idx = findPivot(0,len(nums)-1,nums)
        if nums[pivot_idx] == target:
            return pivot_idx
        if pivot_idx == 0:
            return binary_search(0,len(nums)-1,nums,target)
        if target < nums[0]:    # if target is smaller than leftmost element of array, search the right side of array
            return binary_search(pivot_idx,len(nums)-1,nums,target)
        return binary_search(0,pivot_idx,nums,target)
    
s = Solution()
a = [5,1,3]
t = 0
print(s.search(a,t))


            