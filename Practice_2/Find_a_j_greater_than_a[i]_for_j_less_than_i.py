"""
Traverse the array till 2nd lastg index and compare each element with curr max. If its greater than
current max, then make it curr_max. Then start from this element to the end of the array
if we find any element smaller than current max, then break out of the loop and move 
forward in the array to find an even greater current max
"""

def maxfunction(nums):
    curr_max = float("-inf")
    n = len(nums)
    for j in range(n-1):
        if nums[j] > curr_max:
            curr_max = nums[j]
            for i in range(j+1,n):
                if nums[i] < nums[j]:
                    break
    return curr_max

print(maxfunction([1,2,3,4,5,6,7,8,9,8,7,6,5,13]))