"""Maintain 2 pointers i and j same as in matrix chain multiplication. Length of considered chain is k
consider chains of length k. Chains means window here"""

def Sliding_Window(nums,l):
    n = len(nums)
    output_arr = []
    for i in range(n-l+1):      # i= 0 to n-l
        j = i+l-1               # j = i+l-1
        window = nums[i:j+1]
        max_element = max(window)
        output_arr.append(max_element)
    return output_arr

nums = [1,3,-1,-3,5,3,6,7]

print(Sliding_Window(nums,3))