
from collections import defaultdict
class Solution(object):
    def longestDupSubstring(self, S):
        """
        :type S: str
        :rtype: str
        """
        freq_dict = defaultdict(int)
        #s = list(S)
        n = len(S)
        for l in range(2,n):
            for i in range(n-l+1):
                j = i+l-1
                freq_dict[S[i:j+1]] += 1
        lst = list(freq_dict.items())
        lst.sort(key = lambda x:(x[1],len(x[0])),reverse= True)
        if lst[0][1] > 1:
            return lst[0][0]
        else:
            return ""


s = Solution()
print(s.longestDupSubstring('banananana'))