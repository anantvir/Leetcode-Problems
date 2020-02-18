"""
MAIN IDEA --> Approach 1: Use a queue. Traverse the original matrxi and put every element in the queue. Then traverse the new matrix and on th fly dequeue each
element and assign it to the new matrix.

Approach 2 : 2D matrix can be represented in memory as 1D array. Convert given matrix to 1 D array(temp) where each element of the matrix becomes 
M[i][j] = temp[n*i+j] where n = number of columns and i = index of row in original matrix and j = index of column in original matrix. So make a temp array
then each element in the new Matrix M[p][q] = M[i//c][i%c] where i = each index of temp array. But actually we dont need to create the temp array in
memory because we are not using the array element, just the indices ! which start from 0. So we can just keep a count variable instead which starts from 0.
Now traverse the matrix to be created(given input r and c) and for each index in new matrix, the elemtn at that index is
M_new[i][j] = M_old[count//c][count%c] where c = new number of columns to be expected in output matrix. Then set count ++.
"""

"""--------------------------- Using a Queue ----------------------------"""
from collections import deque
class Solution(object):
    def matrixReshape(self, original_matrix, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        r0 = len(original_matrix)
        c0 = len(original_matrix[0])
        if r0*c0 != r*c:
            return original_matrix
        Q = deque()
        for i in range(r0):
            for j in range(c0):
                Q.append(original_matrix[i][j])
        new_matrix = [[None for i in range(c)]for i in range(r)]
        for i in range(r):
            for j in range(c):
                new_matrix[i][j] = Q.popleft()
        return new_matrix

M = [[1,2,3,4],[5,6,7,8]]
M2 = [[1,2],[3,4]]
s = Solution()
print(s.matrixReshape(M2,1,4))

        