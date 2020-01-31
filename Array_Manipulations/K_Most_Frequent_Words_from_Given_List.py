from collections import Counter
import heapq
class Solution(object):
    """-------------------- Using Sorted List from key,value pairs--------------------"""
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = Counter(words)
        candidates = list(count.keys())
        res = sorted(candidates,key=lambda w:(count[w]),reverse=True)
        return res[:k]

    """--------------------- Using Heap --------------------------"""
    def topKFrequent2(self,words,k):
        counter = Counter(words)
        item_heap = [(-frequencey,word) for word,frequencey in counter.items()] # -ve of frequency because most negative element will be the root of heap
        """
        IMPORTANT --> In heapify we can pass a list of tuples where 1st element of each tuple
        is the one that determines the sort order or heapify order. In this case its
        -ve of frequency(coz heapify generates only min heap) it means highest frequency example -5,-4,-3,-2,-1. 
        -5 will be the root of min heap as its the minimum
        """
        heapq.heapify(item_heap)
        res = []
        for i in range(k):
            word = heapq.heappop(item_heap)[1]     # 1st element of each tuple is the word and 0th element is the frequencey on whose basis heap is formed
            res.append(word)
        return res


words = ["i", "love", "leetcode", "i", "love", "coding"]
words2 = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
s = Solution()
print(s.topKFrequent2(words,2))