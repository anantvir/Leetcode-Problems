"""Maintain 2 pointers i and j same as in matrix chain multiplication. Length of considered chain is k
consider chains of length k. Chains means window here"""


"""--------------- Approach 1    O(N*k)--------------------(Inefficient)"""
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

#print(Sliding_Window(nums,3))


"""--------------- Approach 2 -->O(N)--------------------(Efficient Dynamic Programming)"""

class Solution:
    def Sliding_Window_Max(nums,k):
        n = len(nums)
        if len(nums) == 0:
            raise ValueError("Input array has no data !")
        if k == 1:
            return nums
        left = [0]*len(nums)
        left[0] = nums[0]
        right = [0]*len(nums)
        right[n-1] = nums[n-1]
        for i in range(1,n):
            """--------------- From left to right----------------"""
            if i % k == 0:
                # block start
                left[i] = nums[i]
            else:
                left[i] = max(nums[i],left[i-1])
            """--------------- From right to left ----------------"""
            j = n - i - 1
            if (j+1) % k == 0:
                # Ending of a block
                right[j] = nums[j]
            else:
                right[j] = max(right[j+1],nums[j])
        output = []
        for i in range(n-k+1):                          # Indices in for loop same as matrix chain multiplication
            output.append(max(left[i+k-1],right[i]))    # Indices in for loop same as matrix chain multiplication
        return output

print(Sliding_Window(nums,3))
        