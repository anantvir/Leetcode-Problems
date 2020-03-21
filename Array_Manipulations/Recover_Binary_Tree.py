# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""Main Idea --> Follow 3 steps
1) Computer inorder traversal list
2) The list should be sorted except for 2 elements. Scan the list and find the 2 elements which are not in ascending order
3) Traverse the tree again and whenever we find a node with value = one of the 2 values found above, replace that node with one of the above value.
Keep a counter with initial value =2 and decrement it everytime we replace any nodes value. When counter = 0. We are done !
"""

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return []
        """------------------------- Get inorder traversal array -------------------------------"""
        inorder_list = []
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            inorder_list.append(root.val)
            inorder(root.right)
        inorder(root)

        def getSwappedElems(inorder_list):
            x = y = None
            n = len(inorder_list)
            for i in range(n-1):
                if inorder_list[i+1] < inorder_list[i]:
                    y = inorder_list[i+1]
                    if x == None:
                        x = inorder_list[i]
                        break
            return x,y
        e1,e2 = getSwappedElems(inorder_list)
        
        def traverse(root,count):
            if root:
                if root.val == e1 or root.val == e2:
                    root.val = e2 if root.val == e1 else e1
                    count = count - 1
                    if count == 0:
                        return
                traverse(root.left,count)
                traverse(root.right,count)
        traverse(root,2)
        print('a')
        print('b')

root = TreeNode(10)
root.left = TreeNode(8)
root.right = TreeNode(12)
root.left.left = TreeNode(4)
root.left.right = TreeNode(6)
root.right.left = TreeNode(11)

s = Solution()
print(s.recoverTree(root))
