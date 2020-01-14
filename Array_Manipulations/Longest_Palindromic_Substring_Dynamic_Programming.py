import math

s = 'baabaab'

def Longest_Palindromic_Substring_DP(s):
    max_length = 0
    n = len(s)
    """-----------Memoization Table---------------"""
    table = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        table[i][i] = 1                     # each character is a palindrome so all (i,i) are palindromes
    """------------------------------------------------"""
    s = list(s)
    for l in range(2,n+1):
        for i in range(0,n-l+1):
            j = i+l-1
            if l == 2:          # for length 2 substrings if s[i]=s[i+1] then its a palindrome. Store in table
                if s[i] == s[j]:
                    table[i][j] = 1
            if table[i+1][j-1] == 1:
                if s[i] == s[j]:
                    table[i][j] = 1
                    if j-i+1 > max_length:
                        max_length = j-i+1
    return max_length

print(Longest_Palindromic_Substring_DP(s))