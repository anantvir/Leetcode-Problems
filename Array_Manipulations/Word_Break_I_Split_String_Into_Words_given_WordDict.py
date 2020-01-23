


wordDict = ["leet","code","singh","anantvir"]
s = "leetcodesinghanantvir"

wordDict4 = ["apple","pen"]
s4 = "applepen"

"""-------------------Most Intuitive Dynamic Programming Approach 4--------------------"""
# This works same as matrix chain multiplication starting from considering chains of length = 2 until n
# and checking the substructure of each chain

def Wordbreak4(s,wordDict):
    n = len(s)
    m = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        if s[i] in wordDict:
            m[i][i] = True
        else:
            m[i][i] = False
    for l in range(2,n+1):
        for i in range(n-l+1):
            j = i+l-1
            if s[i:j+1] in wordDict:
                m[i][j] = True
            else:
                for k in range(i,j):
                    if m[i][k] == True and m[k+1][j] == True:
                        m[i][j] = True
    return m[0][n-1]

print(Wordbreak4(s4,wordDict4))


"""------------------ Inefficient Approach 1 --------------------"""
def Wordbreak(s,start):
    if start == len(s):
        return True
    for end in range(start+1,len(s)):
        if s[start:end+1] in wordDict and Wordbreak(s,end+1):
            return True
    return False

"""------------------ Inefficient Approach 2 --------------------"""
def Wordbreak2(s):
    if len(s) == 0:
        return True
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i:j+1] in wordDict:
                s_new = s[:i] + s[j+1:]
                if Wordbreak2(s_new) == True:
                    return True
    return False

"""--------------- Dynamic Programming Approach 3------------------"""
"""Here is for example s = "catsanddogs" then we split it into "catsand" & "dogs". Now both of these strings must
satisfy the constraints i.e they must be optimal substructures. So make an array dp[n] where n represents the 
length of string which can be broken down into dictionary words. dp[0]=True because string of length 0 is always
a member of word dict. Take a pointer i from 1 to len(s). i starts from 1 because i represents length of the string being considered
currently and for i=0 we have already filled the array dp[0]=True. The second pointer j splits the string
of length i into two substrings s1 and s2 such that both of them must also be optimal. We check is s1 is optimal
from the array dp, and check if s2 exists in the given wordDict. If yes then we set dp[i] = True

https://leetcode.com/problems/word-break/solution/
"""
def Wordbreak3(s):
    dp = [False]*(len(s)+1)
    dp[0] = True                # String of length 0 can always be broken into worddict words i.e its always part of worddict
    for i in range(1,len(s)+1):   # i = 1 to len(s) example is s="applepenapple" then i = 1 to 13 where index of last e = 12
        for j in range(0,i):    # j = 0 to i-1
            if dp[j] == True and s[j:i] in wordDict:
                dp[i] = True
                break
    return dp[len(s)]


#print(Wordbreak(s,0))
#print(Wordbreak3(s))