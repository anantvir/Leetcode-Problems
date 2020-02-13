"""Approach --> If its an opening bracket then push it onto the stack. When we encounter
a closing bracket, pop an item from the stack and check if the closing bracket we encountered
is actually the closing bracket of the item we popped from the stack from the
op_clos_dict which is mapping of correct open and close brackets. If the closing bracket
we encountered is not the correct one then no need to check further just return False
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0 or s == ' ':
            return True

        op_clos_dict = {
            '(':')',
            '[':']',
            '{':'}'
        }
        opeing_brackets = ['(','[','{']
        stack = []
        for i in range(len(s)):
            if s[i] in opeing_brackets:
                stack.append(s[i])
            else:
                clos_br = stack.pop()
                if op_clos_dict[clos_br] != s[i]:
                    return False
        return True

s= Solution()
print(s.isValid(' #'))