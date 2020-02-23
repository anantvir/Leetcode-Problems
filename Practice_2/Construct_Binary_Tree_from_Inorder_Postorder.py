"""
Concept is simple. Postorder traversal follows Left->Right->Root. That means the last element in the postorder array is always the root.
When the last element is popped from the postorder array, we find the index of that element in the inorder array. The index we
get from the inorder array splits the inorder array into left and right subtree. Because elements to the left of that index
in the inorder array will be traversed before their root i.e (the index we got) and the right part of the inorder array represents
the right subtree. So increment the index (idx),we found to idx+1 and end remains the same. Recursively build the right subtree.
For left subtree, recursively pass the start index = start and end = idx-1. Below links offer excellent explanation for the problem.

Reference: 
1) https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/solution/
2) https://www.youtube.com/watch?v=s5XRtcud35E
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def buildTree_Helper(start,end):
            if start > end:
                return None
            
            # Current root node
            root_val = postorder.pop()
            root_node = TreeNode(root_val)              # Create a TreeNode for the poped value
            
            # Get index of the popped element from inorder array so that inorder array can be splitted into right and left subtree at the popped element position
            idx = idx_map[root_val]

            # Recursively build right subtree (Because element popped from postorder will always be the last element of postorder array). Hence right subtree will be built first
            root_node.right = buildTree_Helper(idx+1,end)

            # Recursively build left subtree
            root_node.left = buildTree_Helper(start,idx-1)
            
            return root_node

        idx_map = dict()
        for k,v in enumerate(inorder):
            idx_map[v] = k
        root = buildTree_Helper(0,len(inorder)-1)
        return root

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

s = Solution()
s.buildTree(inorder,postorder)