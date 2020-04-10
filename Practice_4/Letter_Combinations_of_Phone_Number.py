class Solution(object):
    """-------------------------------------- Backtracking ---------------------------------------------"""
    """
    Example if input string is "234" then the tree will be like. 1st tree --> root = a, children  = d,e,f. Then for each of
    its children i.e d,e,f, will again have children g,h,i and so on. So we move recursively from  root to the leaf nodes
    of tree and then when we complete a combination i.e len(digits_string) == 0, we append the result to a alist and backtrack
    """
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(combination,dig_string):
            if len(dig_string) == 0:
                res.append(combination)
            else:
                for letter in phone[dig_string[0]]:
                    backtrack(combination + letter, dig_string[1:])

        res = []
        if digits:
            backtrack("",digits)
        return res
