"""------------------------ Brute Force ------------------------"""
from collections import defaultdict
class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.current_sentence = ''
        self.data_dict = defaultdict(int)
        for i in range(len(sentences)):
            self.data_dict[sentences[i]] = times[i]      

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == '#':
            self.data_dict[self.current_sentence] += 1      # If sentence has been completed then add it to data dictionary
            self.current_sentence = ""                      # Reset current sentence because # has been input hence a sentence has ended
        else:
            self.current_sentence += c                      # append new character to characters entered till now
            curr_search_list = []                           # Temporary list to store strings which have starting characters same as the entered sting
            len_curr_word = len(self.current_sentence)
            for key,value in self.data_dict.items():
                if key[:len_curr_word] == self.current_sentence:    # If string entered by user matches with any of the strings in data dictionary, then add it to temporary list
                    curr_search_list.append((key,value))
            sorted_curr_search_list = sorted(curr_search_list,key=lambda x: x[1])   # Sort the list by frequency of search
            if len(curr_search_list) >= 3:                                          # If length is not greater than 3 then just return whatever we have, maybe 2 or 1 search result
                result = sorted(sorted_curr_search_list[-3:],reverse=True,key=lambda x:x[1])
                r = []
                for i in range(len(result)):                # To extract string from tuples like ('ironman',5)
                    r.append(result[i][0])
            else:
                result = sorted(sorted_curr_search_list,reverse=True,key=lambda x:x[1])
                r = []
                for i in range(len(result)):
                    r.append(result[i][0])
            return r
       

# Your AutocompleteSystem object will be instantiated and called as such:
obj = AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
param_1 = obj.input('i')
param_2 = obj.input(' ')
param_3 = obj.input('a')
param_4 = obj.input('#')
print(param_4)