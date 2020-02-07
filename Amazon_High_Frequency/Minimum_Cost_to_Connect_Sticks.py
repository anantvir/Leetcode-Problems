"""
--------------------------------- GREEDY METHOD ------------------------------------------

IMPORTANT--> No Dynamic Programming Required

Create a min heap. Pop top 2 elements from a heap, add them and add their sum to the total cost. Push their sum
i.e X+Y onto the heap. Keep doing this until len(heap array) > 1"""

import heapq
class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        heapq.heapify(sticks)                   # Create min heap
        cost = 0                                # Intial cost
        while len(sticks) > 1:                  # until len(heap array) > 1
            X = heapq.heappop(sticks)           # Pop top 2 elements
            Y = heapq.heappop(sticks)
            cost = cost + X + Y                 # Add to total cost
            heapq.heappush(sticks,X+Y)          # Push the sum of X+Y onto heap because X+Y creates a new stick to which we need to add other sticks. So we need this sum on the heap, we cant just remove it from heap
        return cost                             # Return final cost to merge the sticks into 1 stick. The stick currently in the heap is the final one stick

s = Solution()
print(s.connectSticks([1,8,3,5]))
        