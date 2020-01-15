"""Author - Anantvir Singh, Problem Source - Leetcode, Statement - Rain Water Trapping"""

"""Water stored at particular index i is 
--> minimum of (max height of bar to left of i till start of array, max height of bar towards right of i till end of array )"""



arr = [0,1,0,2,1,0,1,3,2,1,2,1,0]

"""Brute Force Approach  --> Very important to understand why Dynamic Programming is needed"""
def TrapRainWater(height):                             # arr =  array containing elevation at each point(input array)
    total_water_stored = 0
    for i in range(1,len(height)):
        max_left = 0
        for j in range(i,-1,-1):
            max_left = max(height[j],max_left)
        max_right = 0
        for j in range(i,len(height)):
            max_right = max(height[j],max_right)
        water_stored_at_this_index = min(max_left,max_right) - height[i]
        total_water_stored += water_stored_at_this_index
    return total_water_stored

print(TrapRainWater(arr))