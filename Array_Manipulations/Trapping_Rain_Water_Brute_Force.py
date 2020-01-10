"""Author - Anantvir Singh, Problem Source - Leetcode, Statement - Rain Water Trapping"""

"""Water stored at particular index i is 
--> minimum of (max height of bar to left of i till start of array, max height of bar towards right of i till end of array )"""



arr = [0,1,0,2,1,0,1,3,2,1,2,1]

"""Brute Force Approach  --> Very important to understand why Dynamic Programming is needed"""
def TrapRainWater(arr):                             # arr =  array containing elevation at each point(input array)
    total_water_stored = 0
    for i in range(1,len(arr)-1):       # for i = 2 to n-1
        max_left = 0
        for l in range(i-1,-1,-1):     # for l = i+1 to n
            if arr[l] > max_left:
                max_left = arr[l]
        max_right = 0
        for r in range(i+1,len(arr)):
            if arr[r] > max_right:
                max_right = arr[r]
        min_height = min(max_left,max_right)
        if min_height > arr[i]:                     # If height of left or right max height bar > height of index i, then only that index can store water ! --> because its height will be lower than the minimum bar of max height on either left or right i. height of index i < min(max_left,max_right) 
            water_stored_at_i = min_height - arr[i]
            total_water_stored += water_stored_at_i
    return total_water_stored

print(TrapRainWater(arr))