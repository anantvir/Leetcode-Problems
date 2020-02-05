
"""Approach --> For each row of matrix, run a binary search through that row
return True if element is found else False

Complexity --> O(r*log(c)) where r = rows and c = columns"""

"""Better can be done by going through diagnols and searching the row and column
chunks. Refer to https://leetcode.com/problems/search-a-2d-matrix-ii"""

import math
def BinarySearch(value,arr,start,end):
    while start <= end:
        mid = math.floor((start+end)/2)
        if arr[mid] == value:
            return True
        elif value < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False

def Search_2D_Matrix(value,m):
    for i in range(len(m)):
        start_idx = 0
        end_idx = len(m[i])-1
        array = m[i]
        if BinarySearch(value,array,start_idx,end_idx) == True:
            return True
    return False

m =[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
print(Search_2D_Matrix(5,m))