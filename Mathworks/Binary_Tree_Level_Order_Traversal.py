"""---------------- Return List where each element of list is a list of nodes at that level ----------------------------"""

from collections import deque,defaultdict
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level_dict = defaultdict(list)
        Q = deque()
        Q.append((root,0))
        while Q:
            curr_node,curr_level = Q.popleft()
            if curr_node:
                level_dict[curr_level].append(curr_node.val)
                Q.append((curr_node.left,curr_level+1))
                Q.append((curr_node.right,curr_level+1))
        level_list = list(level_dict.items())
        level_list.sort(key=lambda x:x[0])
        res = []
        for i in level_list:
            res.append(i[1])
        return res

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s = Solution()
print(s.levelOrder(root))

        