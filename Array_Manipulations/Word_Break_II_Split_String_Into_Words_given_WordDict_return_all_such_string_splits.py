
"""----------------------- Dynamic Programming using array -------------------------"""
"""dp[k] stores a list of valid strings which can be formed by string of length k taken from the input string.
Example for string "catsanddog", dp[7] stores all the valid strings that can be formed until length 7 of the input string
i.e dp[7] = ["cat sand","cats and"]"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        hashset = set()
        for word in wordDict:
            hashset.add(word)
        dp = [0]*(len(s)+1)
        init = ['']
        dp[0] = init
        for i in range(1,len(s)+1):
            curr_lst = []
            for j in range(0,i):
                print(len(dp[j]))
                if len(dp[j]) > 0 and s[j:i] in hashset:
                    for eachStr in dp[j]:
                        if eachStr == '':
                            curr_lst.append(eachStr + s[j:i])
                        else:
                            curr_lst.append(eachStr + ' ' + s[j:i])
            dp[i] = curr_lst
        return dp[len(s)]

wordDict = ["cat", "cats", "and", "sand", "dog"]
st = "catsanddog"

s = Solution()
print(s.wordBreak(st,wordDict))


def WordBreak_II(s,start):
    res = []
    if start == len(s):
        res.append('')
    for end in range(start,len(s)):
        #print(s[start:end+1])
        if s[start:end+1] in wordDict:
            last = []
            lst = WordBreak_II(s,end+1)
            for string in lst:
                temp = s[start:end+1]
                if string == "":
                    space = ""
                else:
                    space = " "
                res.append(temp+space+string)
    return res
