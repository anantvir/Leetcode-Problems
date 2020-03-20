# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s == None:
            return False
        if t == None:                   # Null tree is a subtree of every other tree
            return True
        if self.isSimilar(s,t):
            return True
        """Recurse on left subtree of s and right subtree of s keeping t same. If at any point a subtree of s matches that of t return True"""
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
    
    def isSimilar(self,s,t):
        if s == None and t == None:             # If s and t are none then they are similar(2 Null trees are similar)
            return True
        if s != None and t != None:             # If neither of them is Null then compare their elements
            if s.val == t.val:
                if self.isSimilar(s.left,t.left) and self.isSimilar(s.right,t.right):
                    return True
        return False                            # If one of them is Null, then obviously they are not similar, return False
        