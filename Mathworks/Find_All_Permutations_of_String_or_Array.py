"""
Approach is Backtracking. For the entire array.string, fix one element and then recurse on the remaining
Then fix second element and then recurse on the remaining. For a detailed and very intuitive explanation

https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/

Recursive function fixes the first element. and then recurses on the remaining string/array
i.e element with position 'l' is fixed, and then permute function os called on the remaining
array starting from l+1
"""
"""IMPORTANT --> value of l decides which value is to remain fixed"""

class Solution:
    def permute(self,nums,l,r):         # l = left index of current array, r = right index of current array
        if l == r:
            print(nums)
        else:
            for i in range(l,r+1):
                self.swap(nums,i,l)
                self.permute(nums,l+1,r)
                self.swap(nums,i,l)

    def swap(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

nums = [1,2,3]
s = Solution()
s.permute(nums,0,len(nums)-1)