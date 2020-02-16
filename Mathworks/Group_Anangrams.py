"""MAIN IDEA --> Sort each element of the given list of strings and convert the sorted
element into a string. Put that string in the hashmap and append that word in the list
corresponding to that key.
Main idea is that anagrams have same characters. If we sort the characters of each word
then all the anagrams will be same and have the same hash value. So store the 
has value as key in hashtable and value = words which have the same value
hashmap = 
{
    HASH VALUE : [LIST OF STRINGS]
    "aet" : ["eat","tea","ate"],
    "ant" : ["tan","nat"],
    "ab" : ["bat"]
}

"""

from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = defaultdict(list)
        for i in range(len(strs)):
            sorted_str = ''.join(sorted(strs[i]))
            hashmap[sorted_str].append(strs[i])
        return list(hashmap.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
print(s.groupAnagrams(strs))