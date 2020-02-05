"""Author - Anantvir Singh, Problem Source - Leetcode, Statemnt - Range Sum Query Immutable"""

"""In these types of problems, caching is the most efficient technique i.e precompute all possible permutations beforehand
and store in a hashtable. Get them is O(1) time from hashtable when required. Although this preprocessing is costly
and has very high space complexity, it is often much faster when number of calls to sumQuery() are very high as given in problem"""

# ------------------ Approach 1 is Brute Force, use a for loop or slice operator in python -------------------

# ------------------- Approach 2 - Caching(Precompute sum for all possible ranges) ------------------------------------

nums = [-2, 0, 3, -5, 2, -1]
dict_sum_range = dict()

def sumQuery(nums):
    n = len(nums)
    for i in range(n):
        Sum = 0
        for j in range(i,n):
            Sum += nums[j]
            dict_sum_range[(i,j)] = Sum
    return dict_sum_range

sumQuery(nums)

print(dict_sum_range[(0,5)])