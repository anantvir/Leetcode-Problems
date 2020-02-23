# """
# We want to search if a substring of particular length exists more than once in the given string.
# We know that if a repating substring of length k exists then a repeating substring of length k-1 also
# exists in s. Therefore we start searching for the maximum length of string which is repeating.
# We can do so by Binary Search--> In this context Binary Search is not searching an element in an array
# like in regular cases. Here, each time we split the string into half, we measure the length of the splitted half
# and check all substrings of that length in the given string 's' and see if any one of them is repeating. If it is repeating, then there
# is a possibility that a larger substring can also be repeating. So we explore the right half of the divided
# subarray and search for longer substrings.
# Since we are dealing with left and right not as indices but as string lengths, we do not need to start from zero
# to make the calculation easier. Although it can be done with zero index also, but starting from 1 makes
# it more intuitive
# """
from collections import defaultdict
class Solution(object):
    
    """----------------------------- Brute Force ------------------------------"""
    """Currently its the best method and gives accurate results for all cases"""
    def LRS(self,s):
        n = len(s)
        freq_dict = defaultdict(int)            # Create ineteger default dict
        for l in range(2,n):                # Same as matrix chain mult create chains for all lengths 
            for i in range(n-l+1):
                j = i+l-1
                freq_dict[s[i:j+1]] += 1        # Increment frequencies
        for k,v in list(freq_dict.items()):
            if freq_dict[k] < 2:            
                freq_dict.pop(k)                # Delete
        lst = list(freq_dict.items())
        lst.sort(key=lambda x:len(x[0]),reverse=True)
        if lst:
            return lst[0][1]
        else:
            return 0


s = Solution()
print(s.LRS('anantabcdanantefghanantijklanantzz'))