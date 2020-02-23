"""
Approach -> Create a set for each row and then put these 3 sets in a list. For every word in
wordlist, make a set of that word. Check if that set(created from word) is a subset of 
any of the sets. If a word is a subset of any of the sets then append it to the result list
"""

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        set1 = set('qwertyuiop')                # Creat a s et for each row
        set2 = set('asdfghjkl')
        set3 = set('zxcvbnm')
        set_list = [set1,set2,set3]             # make a list of sets
        result = []
        for word in words:
            word_as_subset = set(word.lower())  # make a set for each word
            for s in set_list:                  # check if the set created from the word is a subset of any of the sets in the set list
                if word_as_subset.issubset(s):
                    result.append(word)         # if its a subset thenn apend it to the result list
        return result

words = ["Hello", "Alaska", "Dad", "Peace"]
s = Solution()
print(s.findWords(words))