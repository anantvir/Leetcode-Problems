class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""Recursive approach. Recurse the left and right subtrees and keep updating max_sum and price_newpath during each recursive call"""
class Solution:
    def maxPathSum(self, root):
        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0
                
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            price_newpath = node.val + left_gain + right_gain
            
            max_sum = max(max_sum, price_newpath)
        
            return node.val + max(left_gain, right_gain)
   
        max_sum = float('-inf')
        max_gain(root)
        return max_sum

root = TreeNode(-10)
root.left = TreeNode(4)
root.left.left = TreeNode(9)
root.left.right = TreeNode(5)
root.right = TreeNode(-5)

s = Solution()
print(s.maxPathSum(root))

