"""
Approach is really simple although looks complicated. Approach is that at every step, from all 4 directions,
choose the maximum value and put it into queue and mark as visited. Then dequeue it and again from all 4 directions, choose
the maximum value and put into queue and mark as visited. Keep repeating this until you reach the end.
While selecting the maximum value neighbour for each cell, first check if that cell has already been visited or not
i.e cell value != 'V'. If it has not been visited then only enter the if loop in line 38
"""

from collections import deque
class Solution(object):
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        queue = deque()
        queue.append((0,0,A[0][0]))                     # Append 1st element at [0][0] to intialize the queue
        A[0][0] = 'V'
        global_min = float("inf")                       # maitain a global minimum
        rows = len(A)
        cols = len(A[0])
        while queue:
            curr_i,curr_j,curr_val = queue.popleft()                                                        # Pop from queue
            if curr_i != rows-1 and curr_j != cols-1:
                neighbour_i,neighbour_j,neighbour_val = self.getMaxNeighbour(A,curr_i,curr_j,curr_val)      # Get neighbour of current cell popped from queue
                global_min = min(global_min,neighbour_val)                                                  # If current cell has less value then global_min, then update global _min
                A[neighbour_i][neighbour_j] = 'V'                                                           # Mark as visited
                queue.append((neighbour_i,neighbour_j,neighbour_val))                                       # Append in queue
            else:
                return global_min

    def getMaxNeighbour(self,A,i,j,val):
        curr_max = (0,0,float("-inf"))                                                                      # Intialize curr max
        r = len(A)
        c = len(A[0])
        for k in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:                                                         # check in all 4 directions
            if A[k[0]][k[1]] != 'V':                                                                        # If the cell has not been visited already
                if A[k[0]][k[1]] > curr_max[2] and 0 <= k[0] <=r-1 and 0 <= k[1] <= c-1:                    # Check if the current cell is within boundary of grid and has not been already visited and its value is greater than curr_max
                    curr_max = (k[0],k[1],A[k[0]][k[1]])
        return curr_max


grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
s = Solution()
print(s.maximumMinimumPath(grid))