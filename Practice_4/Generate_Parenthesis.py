class Solution(object):
    """Recursive function. Try out all possible parentesis and keep the valid ones. 2^2n are the total number of parenthesis possible. Because we are
    given n pairs of brackets which forms 2n total brackets. Each position can have 2 brackets. So total will be 2^2n where n = pairs or 2^n where n = total
    brackets in n pairs which is = 2n"""
    def generateParenthesis(self, n):
        global_list = []
        def recurse(A):
            if len(A) == 2*n:
                if isValid(A):
                    global_list.append("".join(A))
            else:
                A.append('(')
                recurse(A)
                A.pop()
                A.append(')')
                recurse(A)
                A.pop()

        """Keep a variable bal which increments on seeing ( and decrements on seeing ). If the parenthesisation is valid, bal should be = 0. If its negative or != 0
        then it is invalid parenthesisation. It takes O(n) time where n  = len of one pattern or total number of brackets example for n = 3 it will be ((()))"""
        def isValid(A):
            bal = 0
            for i in range(len(A)):
                if A[i] == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0 
        A = []
        recurse(A)
        return global_list

s = Solution()
n = 3
print(s.generateParenthesis(n))