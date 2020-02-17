"""
MAIN IDEA --> Inorder traversal of a tree is Left > Root > Right, so it will always return
a sorted list in case of BST. So do an Inorder Traversal and check if the returned traversal list
is sorted or not. If not, then return false else true
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []
        def inorder(root):
            curr = root
            stack = []
            while True:
                if curr != None:                # Push instack until you reach leftmost node
                    stack.append(curr)
                    curr = curr.left
                else:
                    if not stack:               # Terminating condition when stack is empty
                        break
                    curr = stack.pop()          # Pop and process the node if no more left children exist
                    res.append(curr.val)
                    curr = curr.right           # Append right child once and then again move to appending left children
            return res
        
        traversal = inorder(root)
        for i in range(len(traversal)-1):
            if traversal[i] > traversal[i+1]:
                return False
        return True

root = TreeNode(10)
root.left = TreeNode(7)
root.right = TreeNode(12)
root.left.left = TreeNode(5)
root.left.right = TreeNode(8)
root.right.left = TreeNode(11)
root.right.right = TreeNode(14)
s = Solution()
print(s.isValidBST(root))





        