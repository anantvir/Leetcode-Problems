# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""----------------------------------- Compute left,leaves and right boundary separately ---------------------------------------"""
class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        """-------------------- If root itself is leaf, just return the root value -----------------------------------"""
        if self.isLeaf(root):
            return [root.val]
        global_list = []
        """-------------------- First append root to global list. Then start left boundary from root.left -----------------"""
        global_list.append(root.val)
        """--------------------------------------------- Left Boundary ----------------------------------------------------"""
        def left_boundary(root):
            if root == None:
                return
            if self.isLeaf(root):
                return
            global_list.append(root.val)
            if root.left:
                left_boundary(root.left)
            else:
                left_boundary(root.right)
        left_boundary(root.left)
        """--------------------------------------------- Leaves ------------------------------------------------------------"""
        def leaves(root):
            if self.isLeaf(root):
                global_list.append(root.val)
            else:
                if root.left:
                    leaves(root.left)
                if root.right:
                    leaves(root.right)
        leaves(root)
        """----------- Since root is already in the left boundary, start right boundary from root.right and not root -----------------"""
        """---------------------------------------------- Right Boundary ---------------------------------------------------"""
        def right_boundary(root):
            if root == None:
                return
            if self.isLeaf(root):
                return
            if root.right:
                right_boundary(root.right)
            else:
                right_boundary(root.left)
            global_list.append(root.val)
        right_boundary(root.right)
        return global_list
        
    def isLeaf(self,node):
        if node.left == None and node.right == None:
            return True
        else:
            return False
    

root = TreeNode(1)
#root.left = TreeNode(2)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)
#root.left.left = TreeNode(4)
# root.left.right = TreeNode(4)
# root.left.right.left = TreeNode(6)
# root.left.right.right = TreeNode(7)
# root.right.left = TreeNode(6)
# root.right.left.left = TreeNode(9)
# root.right.left.right = TreeNode(10)

s= Solution()
print(s.boundaryOfBinaryTree(root))

