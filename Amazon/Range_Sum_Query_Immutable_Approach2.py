"""Author - Anantvir Singh, Problem Source- Leetcode, Statemnt - Range Sum Query Immutable"""

"""In these types of problems, caching is the most efficient technique. Make an array called sum[] where sum[i] represents sum
of elemens from 0 to i-1
Fill up this array. then for given i and j calculate sum[j] - sum [i] to get the result. This procedure is called caching. Instead of 
computing sum for all possible ranges, we save space by computing sum till al values of i in a single array and then calculate
sum from i to j by taking a difference of both index values from sum array"""

# ------------------- Approach 2 - Caching(Calculate sum from 0th value to (i-1)th value and store in an array sum[i]) ------------------------------------

nums = [-2, 0, 3, -5, 2, -1]
Sum = [0]*(len(nums)+1)         # the sum array has length 1 grater than nums array. Because Sum[i] denotes sum till i values. and Sum[0] has no significance, its only initialized for computation
Sum[0] = 0                      # Sum of 1st zero elements is zero

def sumQuery(nums,Sum,i,j):     # i and j are indexes between which we have to find sum
    for k in range(len(nums)):
        Sum[k+1] = Sum[k] + nums[k]
    return Sum[j+1] - Sum[i]    # Sum till index j+1 - sum till ith index

print(sumQuery(nums,Sum,0,2))