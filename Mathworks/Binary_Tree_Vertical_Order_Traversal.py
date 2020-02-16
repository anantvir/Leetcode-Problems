"""MAIN IDEA --> Main idea here is that use BFS and at each iteration, append in the queue (Node,Column). Left child will have
column = curr_col -1 and right child will have col = curr_col + 1. Start with an intial column of of 0 or 1 or any integer it doesnt
matter. Only relative positions matter. Every time you enqueue a node, increase column number by 1 for right child, and decrease
left child column number by 1"""

from collections import deque,defaultdict

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        Q = deque()
        Q.append((root,2))                          # Append (Node,column number), initial column number  = 0 because column number doesnt make a difference its just a reference. Left child will lie to left of it i.e initial-1 and righ will be initial+1
        hashmap = defaultdict(list)
        while Q:
            curr_node,curr_col = Q.popleft()
            if curr_node is not None:                       # If current node is not none then move forward
                hashmap[curr_col].append(curr_node.val)     # It the column number does not exist in the hashmap, then create it, else append to the corresponding list
                if curr_node.left is not None:
                    Q.append((curr_node.left,curr_col-1))
                if curr_node.right is not None:
                    Q.append((curr_node.right,curr_col+1))
        
        item_lst = list(hashmap.items())                    # Hashmap will be like {1 : [9,8,40], 2 : [3,15,12,18] ....}. Sort this by column number  i.e key of this dict and return the values which are lists containing the node values
        item_lst.sort(key=lambda x:x[0])
        res = []
        for elem in item_lst:
            res.append(elem[1])                             # Append only the lists containing node values to the res list
        return res
    
root = TreeNode(3)
n1 = TreeNode(9)
n2 = TreeNode(20)
n3 = TreeNode(15)
n4 = TreeNode(7)
n5 = TreeNode(8)
n6 = TreeNode(6)
n7 = TreeNode(5)
n8 = TreeNode(4)
n9 = TreeNode(12)
n10 = TreeNode(18)
n11 = TreeNode(20)

root.left = n1
root.right = n2
root.right.left = n3
root.right.right = n4
root.right.right.right = n8
root.right.right.left = n7
root.right.left.right = n6
root.right.left.left = n5
root.right.left.left.right = n9
root.right.left.right.left = n10
root.right.right.left.right = n11
s = Solution()
print(s.verticalOrder(root))
        