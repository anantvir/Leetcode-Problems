"""MAIN IDEA, resulting string will start from the largest character in the given string
example leetcode, results is tcode, which starts from t, the largest letter in the given string"""

from collections import defaultdict
class Solution(object):
    """-------------------- Brute Force -------------------------------"""
    def lastSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        hashdict = defaultdict(None)
        for i in range(n):
            for j in range(i,n):
                if s[i:j+1] not in hashdict:
                    hashdict[s[i:j+1]] = 1
        strs = list(hashdict.keys())
        strs.sort()
        return strs

    """--------------------Linear Time Approach -----------------------"""
    """Linear time approach best explained on https://leetcode.com/problems/last-substring-in-lexicographical-order/discuss/369191/JavaScript-with-Explanation-no-substring-comparison-fast-O(n)-time-O(1)-space.-(Credit-to-nate17)
    and https://leetcode.com/problems/last-substring-in-lexicographical-order/discuss/363662/Short-python-code-O(n)-time-and-O(1)-space-with-proof-and-visualization
    Basic idea is that maintain 3 pointers i,j and k. i always points to the current best substring i.e current substring which 
    should be last in lexicographical order. j represents the current candidate substrinig being tested.
    if s[i] and s[j] match, then k is incremented(until s[i] and s[j] match, k remains zero) and next characters 
    i+k and j+k are compared. If at any time s[i+k] > s[j+k] then j is set to j+k+1, because upto j+k characters
    have already been tested. If s[i+k] < s[j+k] that means s[j+k:] will be better than the current substring
    represented by s[i:]. So now i needs to be moved to a new position which represents the better substring.
    So i will now be  moved to j i.e i = j if if j is still further ahead of i+k. Else if i+k has already crossed j, 
    then i is set to i+k+1 and not j+k because j does not always necessarily comes after i always. For example
    in string 'hhhccchhhddd' when i=0,j=6 and k=3 we set i = j and for string 'nnnp' when i=0,j=1 and k=2, we set
    i = i+ k + 1"""
    def lastSusbtring2(self,s):
        n = len(s)
        i = 0
        j = 1                               # Intially j points to index next to i
        k = 0
        while j + k < n:                    # While j+k remains inside the string
            if s[i+k] == s[j+k]:            # k is incremented only if s[i] and s[j] match
                k += 1
                continue                    # If s[i] == s[j] then start comparing next letters
            elif s[i+k] > s[j+k]:           # if s[i+k] > s[j+k] then 
                j = j + k + 1
            else:
                i = max( j, i + k + 1)
                j = i + 1
            k = 0
        return s[i:]      

s = Solution()
print(s.lastSubstring2('tcotdetco'))
