"""Here we can consider different words of word list to be nodes of a graph and edges represent change of 1 character between
word in one node and the word in the other node i.e https://leetcode.com/problems/word-ladder/solution/
We can use BFS to reach the desired node in this graph thus finding shortest path

How to fins words which can change by only 1 character ? 
Add a wild card '*' and get all possible generic states example all generic states of dog can be represented as
*og
d*g
do*
Store these intermediate/generic states in a dictionary example 
all_combination_dict =
{
    *og :[dog,log,cog]
    d*g :[dog]
    do* :[dot,dog]
}
put a tuple (beginWord,1) where 1 represents level of graph for BFS in the queue. Then start dequeing and for each
dequeued word, check all adjacednt nodes of this word by checking the all_combination_dict. If they have been visited before then
just clear that list else append them in queue and continue running BFS
"""

from collections import defaultdict,deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        # Since all words have same length
        L = len(beginWord)
        # Dict to hold all generic states of a particular word in wordlist
        all_combinations_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is generic word and Value is list of words which have same intermediate/generic word
                all_combinations_dict[word[:i]+"*"+word[i+1:]].append(word)

        queue = deque([(beginWord,1)])      # Initial Tuple containing (word,level)

        """Visited dict so that we dont repeat processing the same node and appending it again in the queue
        It prevents cycles in the resulting graph"""
        visited = {beginWord:True}          

        while queue:
            curr_word,curr_level = queue.popleft()

            for i in range(L):
                intermediate_word = curr_word[:i]+"*"+curr_word[i+1:]
                for word in all_combinations_dict[intermediate_word]:
                    if word == endWord:
                        return curr_level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word,curr_level + 1))
                all_combinations_dict[intermediate_word] = []       # Clear the list for that intermediate word because those intermediate words have been processed and visited, they should not be visted again   
        return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

obj = Solution()
print(obj.ladderLength(beginWord, endWord, wordList))
        