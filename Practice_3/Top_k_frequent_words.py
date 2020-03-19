import heapq
from collections import defaultdict
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        """Create a dict with key = word and value = count. After that create a heap and push each tuple on the heap where 
        tuple = (- frequency,word). heap will heapify based on order of elements in the tuple. 1st it will sort by frequency,
        then by word"""
        if len(words) == 0:
            return []
        dic = defaultdict(int)
        for word in words:
            dic[word] += 1
        lst = list(dic.items())
        heap = []
        for elem in lst:
            heapq.heappush(heap,(-elem[1],elem[0]))
        lst = []
        for j in range(k):
            lst.append(heapq.heappop(heap)[1])
        return lst

s = Solution()
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(s.topKFrequent(words,k))


