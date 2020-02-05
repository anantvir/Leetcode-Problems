"""Author - Anantvir Singh, Problem Source - Leetcode, Statement - Rain Water Trapping"""

"""https://leetcode.com/problems/trapping-rain-water/solution/"""
"""take 2 arrays l and r.  l[i] contains max height of bar starting from leftmost element of array to index i
r[i] contains max height of bar starting from rightmost element of array to index i
Choose minimum of these and subtract height of bar at index i from it. Add that to answer"""

arr = [0,1,0,2,1,0,1,3,2,1,2,1]

def TrapRainWater_DynamicProg(arr):
    total_water = 0
    l = [0]*len(arr)
    r = [0]*len(arr)
    l[0] = 0                                       # Initialize it beforehand
    r[len(arr)-1] = arr[-1]                        # Initialize it beforehand
    for i in range(1,len(l)):                      # i = 1 to n, because l[0] already has 0 height. Initialize it before iterating the array
        max_till_now = max(l[i-1],arr[i])
        l[i] = max_till_now
    for i in range(len(arr)-2,-1,-1):               # i = n-1 to 0, because r[n] has already been set to last value of arr
        max_till_now = max(r[i+1],arr[i])
        r[i] = max_till_now
    for i in range(len(arr)):
        min_bar_height = min(l[i],r[i])             # Choose min from l and r. i.e minimum height bar till index i from left and from right
        if min_bar_height > arr[i]:                 # if min height bar > element at index i, only then there will be a downward pocket created to store water
            capacity = min_bar_height - arr[i]
            total_water += capacity
    return total_water
    
print(TrapRainWater_DynamicProg(arr))
     


