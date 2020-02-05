"""-------------------------- Tree Just for Testing Actual Code is below this tree -----------------"""

class BinarySearchTree:
    # Nested class because it is only locally required inside BinarySearchTree class
    class Node:
        def __init__(self,val,parent =None,left = None,right = None):
            self.val = val
            self.parent = parent
            self.left = left
            self.right = right
        
    def __init__(self):
        self.root = None
        self.size = 0
        self.CURR_PTR = None
    
    def findBST(self,item):
        if self.root is None:                           # Tree empty ?
            LOCATION = None
            PARENT = None
            return LOCATION,PARENT
        if item == self.root.val:                      # Item at root ?
            LOCATION = self.root
            PARENT = None
            return LOCATION
        self.CURR_PTR = self.root
        if item < self.root.val:                       # Item less than root ? move to left subtree
            self.CURR_PTR = self.CURR_PTR.left
            SAVE = self.root
        else:                                           
            self.CURR_PTR = self.CURR_PTR.right   # Item greater than root ? move to right subtree
            SAVE = self.root
        while self.CURR_PTR is not None:
            if item == self.CURR_PTR.val:
                LOCATION = self.CURR_PTR
                PARENT = SAVE
                return LOCATION,PARENT 
            if item < self.CURR_PTR.val:
                SAVE = self.CURR_PTR
                self.CURR_PTR = self.CURR_PTR.left
            else:
                SAVE = self.CURR_PTR
                self.CURR_PTR = self.CURR_PTR.right
        LOCATION = None
        PARENT = SAVE
        return LOCATION,PARENT
    
    def insertBST(self,item):
        LOC_PAR = self.findBST(item)                                # search if item already exists in tree ?
        if LOC_PAR[0] is not None:
            print('Node already exists at location :',LOC_PAR[0])   # If it exists, print it
        newNode = self.Node(item)                                   # Else, create new node if does not exist
        if LOC_PAR[1] is None:                                      # make it root is no root exists already
            self.root = newNode
        elif item < LOC_PAR[1].val:                                # insert item at left or right as per BST logic
            LOC_PAR[1].left = newNode
        else:
            LOC_PAR[1].right = newNode
        return newNode
"""-----------------------------------------------------------------------------------------------"""
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if t == None:
            return True
        if s == None:
            return False
        if self.isIdentical(s,t):
            return True
        result = self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
        return result
    
    def isIdentical(self,root_t1,root_t2):
        if root_t1 == None and root_t2 == None:
            return True
        if root_t1 != None and root_t2 != None:
            if root_t1.val == root_t2.val:
                if self.isIdentical(root_t1.left,root_t2.left) and self.isIdentical(root_t1.right,root_t2.right):
                    return True
        return False


t = BinarySearchTree()
root = t.insertBST(80)
t.insertBST(40)
t.insertBST(30)
t.insertBST(15)
t.insertBST(32)
t.insertBST(36)
t.insertBST(35)
#t.insertBST(37)
t.insertBST(90)
t.insertBST(85)
t.insertBST(100)

subtree = BinarySearchTree()
root_t = subtree.insertBST(30)
subtree.insertBST(15)
subtree.insertBST(32)
subtree.insertBST(36)
subtree.insertBST(35)

s = Solution()
print(s.isSubtree(root,root_t))
        