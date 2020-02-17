"""
MAIN IDEA --> Use a stack. Initially push root onto stack. Then for every popped element(curr), if it has left child and left child
is a leaf, then add it to the sum. Else push the left child onto stack. And for the same popped element, if it has right
child and right child is a leaf, DO NOT append it to stack, but if its not a leaf, then append it to stack.
Do this inside a while loop until the stack is not empty
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        curr = root
        stack = []
        stack.append(root)
        sum = 0
        while stack:
            curr = stack.pop()
            """------------ Check if popped node has a left child and left is leaf -----------------"""
            if curr.left:
                if curr.left.left == None and curr.right.right == None:
                    sum += curr.left.val
                else:
                    # Push current on stack
                    stack.append(curr.left)
            """------------ Check if popped node has a right child and if right is not leaf then append to stack -----------------"""
            if curr.right:
                if curr.right.right != None or curr.right.left != None:
                    stack.append(curr.right)
        return sum

root = TreeNode(10)
root.left = TreeNode(7)
root.right = TreeNode(12)
root.left.left = TreeNode(5)
root.left.right = TreeNode(8)
root.right.left = TreeNode(11)
root.right.right = TreeNode(14)
s= Solution()
print(s.sumOfLeftLeaves(root))
        

        

        