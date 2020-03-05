"""
Main Idea --> Sliding Window Approach. Keep 2 pointers i and j. Everytime we encounter a new j
check if it exists in the hashset or not. If it does not exist then add it to hashset and and icrement j. Else if it 
exists, then remove s[i] from set and increment i. Do this while i < n and j < n because once j is greater than n
we can no longer compare if s[j] is present in hashset or not !
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = 0
        j = 0
        max_len = 0
        hashet = set()
        while i < n and j < n:
            if s[j] not in hashet:
                hashet.add(s[j])
                max_len = max(max_len,j-i+1)
                j += 1
            else:
                hashet.remove(s[i])
                i += 1
        return max_len

a = "abcabcbb"
s = Solution()
print(s.lengthOfLongestSubstring(a))
