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

"""-----------------------------------------------------------------------------------------------------"""

class Solution(object):
    def __init__(self,root):
        self.root = root

    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        """-------------------- Left Boundary --------------------------"""
        def left_boundary(root):
            curr_ptr = root
            while curr_ptr.left != None or curr_ptr.right != None:
                if curr_ptr.left != None:
                    res.append(curr_ptr.val)
                    curr_ptr = curr_ptr.left
                else:
                    res.append(curr_ptr.val)
                    curr_ptr = curr_ptr.right
        
        """------------------- Leaf Nodes ------------------------------"""
        def isLeaf(node):
            if node.left == None and node.right == None:
                return True
            else:
                False
        def findLeaves(root):
            if isLeaf(root):
                res.append(root.val)
                #return
            else:
                if root.left:
                    findLeaves(root.left)
                if root.right:
                    findLeaves(root.right)

        """------------------- Right Boundary ----------------------------"""
        def right_boundary(root):
            if root.right:
                curr_ptr = root.right
            stack = []
            while curr_ptr.right != None or curr_ptr.left != None:
                if curr_ptr.right != None:
                    stack.append(curr_ptr.val)
                    curr_ptr = curr_ptr.right
                else:
                    stack.append(curr_ptr.val)
                    curr_ptr = curr_ptr.left
            while len(stack) > 0:
                item = stack.pop()
                res.append(item)

        left_boundary(self.root)
        findLeaves(self.root)
        right_boundary(self.root)
        return res

t = BinarySearchTree()
root = t.insertBST(30)
t.insertBST(15)
t.insertBST(10)
t.insertBST(5)
t.insertBST(3)
t.insertBST(8)
t.insertBST(7)
t.insertBST(9)
t.insertBST(11)
t.insertBST(18)
t.insertBST(17)
t.insertBST(20)
t.insertBST(50)
t.insertBST(40)
t.insertBST(35)
t.insertBST(45)
t.insertBST(43)        

sol = Solution(root)   
print(sol.boundaryOfBinaryTree(root))
