"""
MAIN IDEA --> Backtracking. Fix the 1st element by swapping i th element with l th element,
then recurse one the remaining array. At each recursive call, fix the 1st element and recurse
on the remaining. Folow this until  l == r.
Also after the recursive call, swap the elements again to take array elements to the same position
as before
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        A = nums
        res = []
        def recurse(A,l,r):
            if l == r:
                res.append(A)
            else:
                for i in range(l,r+1):
                    self.swap(A,i,l)
                    recurse(A,l+1,r)
                    self.swap(A,i,l)
        recurse(A,0,len(A)-1)
        return res

    def swap(self,A,i,j):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp

a = [1,2,3]
s = Solution()
print(s.permute(a))