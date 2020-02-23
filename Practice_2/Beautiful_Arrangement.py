class Solution(object):
    """------------ Approach 1 (Brute Force Highly Inefficient) O(n*n!) ------------------"""
    """Get all possible permutations from the given numbers from 1 to N.
    Check each permutation if it satisfies the given constraints
    IMPORANT--> Learn how to get permutations of given numbers/string
    """
    count = 0                           # Count the number of beautiful arrangements
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        nums = [0]*N
        n = len(nums)
        for i in range(1,N+1):
            nums[i-1] = i
        self.permute(nums,0,n-1)
        return Solution.count

    def permute(self,nums,l,r):         # l = left index of current array, r = right index of current array
        n = len(nums)
        if l == r:
            for i in range(1,n+1):
                if nums[i-1] % i != 0 and i % nums[i-1] != 0:
                    break
                if i == n:
                    Solution.count += 1
        else:
            for i in range(l,r+1):
                self.swap(nums,i,l)
                self.permute(nums,l+1,r)
                self.swap(nums,i,l)
    
    def swap(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    
    """----------------- Approach 2 Brute Force Optimized ---------------"""
    """
    The above O(n*n!) complexity can be drastically reduced. How ??---> In Brute Force,
    we create every possible array and then check the array for divisibility constraints.
    But while creating the array and adding every element in the array(While creating the
    permutation), we can check if adding the above element will violate the divisibility
    constraints or not. If it does then skip that iteration or that permutation. Its
    complexity will be O(k) where k is no. of valid permutations.
    While adding a new element, we always swap the current element with 'L'. So during
    each iteration, after swapping the first time, we need to check if item at position
    L is divisible by position L(position is given by L+1 because L is index which starts
    from zero) or not. Hence nums[L] % (L+1) 
    """
    def countArrangement_Optimized(self,N):
        nums = [0]*N
        n = len(nums)
        for i in range(1,n+1):
            nums[i-1] = i
        self.permute_optimized(nums,0,n-1)
        return Solution.count
    
    def permute_optimized(self,nums,l,r):
        n = len(nums)
        if l == len(nums):
            Solution.count += 1
        else:
            for i in range(l,r+1):
                self.swap_new(nums,i,l)
                if nums[l] % (l+1) == 0 or (l+1) % nums[l] == 0:
                    self.permute_optimized(nums,l+1,r)
                self.swap_new(nums,i,l)

    def swap_new(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

s = Solution()
print(s.countArrangement_Optimized(3))