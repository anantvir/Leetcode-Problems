"""https://leetcode.com/problems/132-pattern/

in a given list a1,a2 ..... an   i<j<k and a_i < a_k < a_j. Return all possible subsequences.
Note they are subsequences not substring so they dont need to be consecutive

"""

class Solution(object):
    """------------------------ Brute Force O(n^3) ------------------------"""
    def find132pattern_1(self, nums):
        n = len(nums)
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if nums[k] > nums [i] and nums[j] > nums[k]:
                        return True
        return False

    """------------------------ Improved Brute Force O(n^2) ------------------------"""
    """ Since we only have to return True or False, we can just choose i to be the minimum element
    found so far before the index j. Then we just need to search beyond j to find a k > j > i such that
    nums[i] < nums[k] < nums[j] (given condition) !
    We keep track of minimum value of nums[i], then for a particular value of nums[j], we just need
    to find a nums[k] > nums[i] and less than nums[j]. This can be found by traversing nums beyond j.
    Thus the first for loop in approach 1 vanishes !"""

    def find132pattern_2(self,nums):
        n = len(nums)
        min_i = float("-inf")
        for j in range(n-1):
            min_i = min(min_i,nums[j])
            for k in range(j+1,n):
                if nums[k] < nums[i] and min_i < nums[k]:
                    return True
        return False

obj = Solution()
#print(obj.find132pattern_1([-1, 3, 2, 0]))
