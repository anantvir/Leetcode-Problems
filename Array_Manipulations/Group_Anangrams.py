"""Author - Anantvir Singh, Problem Source - Leetcode, Statement -> Group Anagram"""

"""Anagrams contain same count of characters, example "ate" contains 1 a, 1 t and 1 e. So we count the number of characters in each
string and put them in a tuple containing 122 total elements. So tuple for ate will look like (0,0,...97,0,0,116,...,101,0,0)
Why 122 total elements ? --> because unicode value of a = 97 and z = 122. Put this tuple as key of a dict, so whenever for any string we will have
the same tuple, it will be stored in the list corresponding to the same key example 'ate' will have same tuple of 122 elements as 'tea'"""

import collections

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

answer = collections.defaultdict(list)

def Group_Anagrams(words):
    for word in words:
        count = [0]*122
        for character in word:
            count[ord(character)] += 1
        answer[tuple(count)].append(word)               # dictionary keys cannot be lists as lists are unhashable types, so create tuples
    return answer.values()

print(Group_Anagrams(words))




