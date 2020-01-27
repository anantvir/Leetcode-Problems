"""--------------------- Approach 1 Just do what the question says. Sort the array and find median----------------"""

import math
class MedianFinder:
    def __init__(self):
        self.nums = []

    def addNum(self,num):
        self.nums.append(num)
        return self.nums

    def median(self):
        self.nums = sorted(self.nums)
        n = len(self.nums)
        if n % 2 == 0:
            mid = int(n/2) - 1
            median = (self.nums[mid] + self.nums[mid+1])/2
        else:
            mid = math.floor(n/2)
            median = self.nums[mid]
        return median

m = MedianFinder()
m.addNum(8)
m.addNum(34)
m.addNum(2)
m.addNum(7)
m.addNum(78)
m.addNum(13)
m.addNum(10)

#print(m.median())
"""---------------- Approach 2 --> Use 2 heaps, Max heap and Min heap ---------------------------"""

"""max_heap stores lower n/2 elements. Its root returns max(n/2 th element)
min_heap stores upper n/2 elements. Its root returns n/2 the or n/2+1 th element

Whenever you get a new element first push it onto max_heap so that it can sink to its appropriate position if its smaller than root
then pick the top element of max_heap and push it onto min_heap. The check if min_heap.size() > max_heap.size().
If yes, then push the top of min_heap onto top of max_heap(Since max heap can have at most one element
more than min heap)
If size of both min and max heap is same then median = (top of both heaps)/2 else if size of max heap  > min heap
median =  top of Max heap !"""

"""IMPORTANT --> No function/module for Max heap in python"""

