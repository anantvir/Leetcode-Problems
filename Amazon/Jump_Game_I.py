"""Author - Anantvir Singh, Problem Source - Leetcode , Statement -> Jump Game"""

"""Each position of nums array i.e nums[i] gives maximum number of steps you can take from that index. example if nums[i] = 3,
it means you can take 3,2 or 1 step from position i. Obviously 0 step from i doesnt make any sense"""

"""Brute Force, at each position i, check nums[i], calculate maximum number if jumps allowed, which is minimum of 
(position+nums[position] and last index of array). Then """

arr = [2,3,1,1,4]
arr1 = [3,2,1,0,4]


"""Brute Force  O(2^n)--> Exponential"""
def Can_Jump_from_Position(position,nums):
    if position == len(nums) - 1:
        return True
    max_jumps = min(position+nums[position],len(nums)-1)
    for newPosition in range(position+1,max_jumps+1):
        if Can_Jump_from_Position(newPosition,nums):
            return True
    return False

def Can_Jump(nums):
    return Can_Jump_from_Position(0,nums)

print('Brute Force Result :',Can_Jump(arr1))



"""Dynamic Programming Memoization   O(n^2)"""

memo = [None]*len(arr)                              # memo[-1] = good index since we can reach last index from itself(trivial)
memo[-1] = 'Good'
def Can_Jump_From_Position_DP(curr,arr):
    if memo[curr] == 'Good':                        # check if current index is good or bad, if good then return true because we know we can reach end from this index because its a good index
        return True
    if curr == len(arr)-1:                          # if curr not in memoized array then run the recursive function again
        return True
    farthestJumpAllowed = min (curr + arr[curr],len(arr)-1)
    for next_position in range(curr+1,farthestJumpAllowed+1):
        if Can_Jump_From_Position_DP(next_position,arr):
            memo[curr] = 'Good'
            return True
    memo[curr] = 'Bad'
    return False

def Driver_Function(arr):
    return Can_Jump_From_Position_DP(0,arr)

print('Dynamic Programming Solution :',Driver_Function(arr1))



