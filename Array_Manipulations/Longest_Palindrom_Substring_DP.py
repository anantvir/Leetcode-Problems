"""Author - Anantvir Singh, Problem Source - Leetcode, Statement - Longest Palindrome Substring"""

"""Using Dynamic Programming. because if already know that aba is palindrome and store it in a matrix/array etc and we get a new string
s = xabax where i=x and j=x, then we can check if matrix[i+1][j-1] already has a palindrome. If yes then we just need to check
if s[i]==s[j]. If yes then we have a new longer palindrome from a previously stored result"""

"""Consoder chains of length l=2 to n same as in matrix chain multiplication"""

s = 'baabbaac'

def Longest_Palindrome_Substring(s):
    n = len(s)
    P = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            P[i][i] = 1
    for l in range(2,n):            # l = 2 to n
        for i in range(n-l+1):      # i = 1 to n-l+1
            j = i+l-1
            if l == 2:
                if s[i] == s[j]:
                    P[i][j] = 1
            else:
                if P[i+1][j-1] == 1:
                    if s[i] == s[j]:
                        P[i][j] = 1
    return P

print(Longest_Palindrome_Substring(s))

