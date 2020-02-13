#Definition for a binary tree node.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""Can be done via BFS and DFS both
Create a level dict {level : rightmost node corresponding to that level}
for DFS --> (DFS is not recursive here, rather it uses stack) Push root onto stack, then while stack is not empty. Check the popped not if exists. If yes then check if that level already exists in the dict. If yes then dont add to dict else add to dict
BFS --> Its almost same as DFS, except that in BFS due to quque we have to process all the nodes. For each processed node, we only keep the last processd node in each level. Because that will
give the righmost node required. Hence in the dict, remove the check where we check if that level already has a corresponding node or not.
"""
from collections import deque
class Solution(object):
    def rightSideView_DFS(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """------------- Use stack for DFS and push left child on stack first and then right and then pop during next iteration-----------"""
        def DFS(root):
            stack = []
            level_dict = dict()
            max_depth = -1
            stack.append((root,0))
            while stack:
                node,depth = stack.pop()
                if node is not None:
                    max_depth = max(max_depth,depth)
                    if depth not in level_dict:
                        level_dict[depth] = node.val
                    stack.append((node.left,depth+1))
                    stack.append((node.right,depth+1))
            return list(level_dict.values())
        return DFS(root)
    
    """------------- Use queue for BFS and keep only rightmost element -----------"""
    def rightSideView_BFS(self, root):
        queue = deque()
        level_dict = dict()
        max_Depth = -1
        queue.append((root,0))
        while queue:
            node,depth = queue.popleft()
            max_Depth = max(max_Depth,depth)
            if node is not None:
                level_dict[depth] = node.val        # No need to check if the node for that depth already exists or not. Overwrite the old value as the rightmost node will always be visited at last during BFS
                queue.append((node.left,depth+1))
                queue.append((node.right,depth+1))
        return list(level_dict.values())

root = Node(1)
root.left=Node(2)
root.right = Node(3)
root.right.right = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(7)
root.left.right.right.right = Node(8)
root.left.right.left = Node(6)
s = Solution()
print(s.rightSideView_BFS(root))


        