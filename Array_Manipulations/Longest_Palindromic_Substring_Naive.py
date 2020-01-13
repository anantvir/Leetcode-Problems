"""Naive Solution. Should be done with DP"""


import math

s = 'anantvirbaattaabtanana'

def Longest_Palindromic_Substring_Naive(s):
    max_length = 0
    l = list(s)
    for i in range(0,len(l)-1):             # Check all possible strings. From i = 0 to 2nd last element of array and j = i+1 to last element of array
        for j in range(i+1,len(l)):
            if Is_Palindrome(l,i,j):
                if j-i+1 > max_length:
                    max_length = j-i+1
    return max_length

def Is_Palindrome(s,i,j):       # Regualar function to check for palindrome
    temp_str = s[i:j+1]
    n = len(temp_str)
    for i in range(0,math.floor(n/2)):
        if temp_str[i] != temp_str[n-i-1]:
            return False
    return True

print(Longest_Palindromic_Substring_Naive(s))