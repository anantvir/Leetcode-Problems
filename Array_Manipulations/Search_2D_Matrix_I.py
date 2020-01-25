"""----------- Since each row of matrix is sorted, all the rows can be considered to be a single sorted array
and then apply Binary Search -------------------------"""


matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

import math
def Search_2D_Matrix(value,m,start,end):
    r = len(matrix)
    c = len(matrix[0])
    mid = math.floor((start+end)/2)
    mid_r = mid // c
    mid_c = mid % c
    if start > end:
        return False
    if value == m[mid_r][mid_c]:
        return True                                 # Optionally return the index tuple (i,j) of the element as well
    elif value < m[mid_r][mid_c]:
        return Search_2D_Matrix(value,m,start,mid-1)
    elif value > m[mid_r][mid_c]:
            return Search_2D_Matrix(value,m,mid+1,end)

end_index = len(matrix)*len(matrix[0])-1            # rows * columns - 1
print(Search_2D_Matrix(50,matrix,0,end_index))       