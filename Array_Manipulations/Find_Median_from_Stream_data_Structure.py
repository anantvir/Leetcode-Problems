import heapq
class MedianFinder(object):

    """----------------------------------- Efficient 2 heap approach -----------------------------"""
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.low = []
        self.high = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.low,-num)
        positive_num = - heapq.heappop(self.low)
        heapq.heappush(self.high,positive_num)
        if len(self.high) > len(self.low):
            elem = heapq.heappop(self.high)
            heapq.heappush(self.low,-elem)          # Push -ve of elem rather than elem as python does not have inbuilt Max Heaps !!

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.low) == len(self.high):
            low_top = -heapq.heappop(self.low)
            heapq.heappush(self.low,-low_top)
            high_top = heapq.heappop(self.high)
            heapq.heappush(self.high,high_top)
            return (low_top+high_top)*0.5
        else:
            low_top = -heapq.heappop(self.low)
            heapq.heappush(self.low,-low_top)
            return low_top

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()