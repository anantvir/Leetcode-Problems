"""MAIN IDEA
--> If a sub array still has same degree as the original array that means there are some
elements in the sub array which have same frequency as the maximum frequencey in the given
array. Therefore we can record the indices of the first occurence of each element
and last occurence of each element in a hashtable/dict. 
The dict left will store staring values of each element in the array
e.g left[2] = 1 means that 1st occurence of 2 is at index 1
right[3] = 3 means last occurence of 3 is at index 3
Then we can find the min length sub array by just choosing the minimum value from
left[x] - right[x] + 1 (+1 to include the 1st element)
"""

from collections import defaultdict
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """  
        """Traverse the array once and record left,right and frequency dicts"""
        freq_dict = defaultdict(int)
        left_dict = defaultdict(int)
        right_dict = defaultdict(int)
        n = len(nums)
        for i in range(n):
            freq_dict[nums[i]] += 1                     # increase frequency
            if nums[i] not in left_dict:
                left_dict[nums[i]] = i                  # store in left only if its not present because it will only store the fisrt occurence index. for 2nd or consecutive occurence it will not go inside the for loop
            right_dict[nums[i]] = i
        degree = max(freq_dict.values())
        ans = len(nums)                                 # Maximum length possible = len of given array
        for key in freq_dict:
            if freq_dict[key] == degree:
                ans = min(ans,right_dict[key] - left_dict[key] + 1)
        return ans

nums = [1,2,2,3,1]
nums2 = [1,2,2,3,1,4,2]
s = Solution()
print(s.findShortestSubArray(nums2))