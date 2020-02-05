"""Author - Anantvir Singh, Problem Source - Leetcode, Statement -- > Group Anangrams"""

from collections import defaultdict

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

def Group_Anagrams(words):
    ans = defaultdict(list)
    for word in words:
        ans[tuple(sorted(word))].append(word)
    return ans.values()

print(Group_Anagrams(words))


