import math
class Solution(object):

    """---------------------- Brute Force O(n^2) -------------------------"""
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        min_dist = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                for j in range(len(words)):
                    if words[j] == word2:
                        dist = abs(j - i)
                        min_dist = min(dist,min_dist)
        return min_dist
    
    """----------------------- Linear O(n) --------------------------"""
    def shortestDistance_Linear(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        pointer_1 = -1
        pointer_2 = -1
        min_dist = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                pointer_1 = i
            if words[i] == word2:
                pointer_2 = i
            if pointer_1 != -1 and pointer_2 != -1:
                dist = abs(pointer_2 - pointer_1)
                min_dist = min(min_dist,dist)
        return min_dist


words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = 'makes'
word2 = 'coding'
s = Solution()
print(s.shortestDistance_Linear(words,word1,word2))