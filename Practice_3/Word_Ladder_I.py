from collections import defaultdict
from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if len(wordList) == 0 or not beginWord or not endWord:
            return 0
        L = len(beginWord)      # Because L remains same for all words. This is used to create generic states for each word
        intermediate_states_dict = defaultdict(list)

        """------------------------------ Create dictionary for intermediate states ------------------------------------"""
        for word in wordList:
            for i in range(L):
                intermediate_word = word[:i] + '*' + word[i+1:]
                intermediate_states_dict[intermediate_word].append(word)
        
        """------------------------------------------------- Run BFS ---------------------------------------------------"""
        Q = deque()
        Q.append((beginWord,1))
        visited = {beginWord : True}
        while Q:
            curr_word, curr_level = Q.popleft()
            for i in range(L):
                intermediate_word = curr_word[:i] + '*' + curr_word[i+1:]
                for word in intermediate_states_dict[intermediate_word]:
                    if word == endWord:
                        return curr_level + 1
                    if word not in visited:
                        visited[word] = True
                        Q.append((word,curr_level + 1))
        return 0
                        


        