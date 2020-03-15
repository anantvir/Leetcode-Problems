from collections import defaultdict
class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.sent_freq_dict = defaultdict(int)
        self.curr_sent = ''
        for i in range(len(sentences)):
            self.sent_freq_dict[sentences[i]] = times[i]

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == '#':
            self.sent_freq_dict[self.curr_sent] += 1
            self.curr_sent = ''
        else:
            self.curr_sent += c
            L = len(self.curr_sent)
            temp_lst = []
            for k,v in self.sent_freq_dict.items():
                if k[:L] == self.curr_sent:
                    temp_lst.append((k,v))
            temp_lst.sort(key = lambda x : (-x[1],x[0]),reverse=True)
            l = []
            for item in temp_lst:
                if len(l) == 3:
                    return l
                else:
                    l.append(item[0])
            return l

obj = AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
param_1 = obj.input('i')
param_2 = obj.input(' ')
param_3 = obj.input('a')
param_4 = obj.input('#')
print(param_4)
