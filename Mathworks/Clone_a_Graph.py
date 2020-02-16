"""MAIN IDEA --> Can eb done with BFS or DFS, we just need to maintain a visited dictionary where key = original node which has just
been visited and value = its cloned copy (cloned = Node(original_node.val,[])). Rest of the process is similar for BFS"""

from collections import deque

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        visited = dict()
        Q = deque()
        Q.append(node)
        visited[node] = Node(node.val,[])

        """------------------------------ BFS -------------------------------------"""
        
        while Q:
            curr_node = Q.popleft()
            for neighbour in curr_node.neighbors:
                if neighbour not in visited:
                    visited[neighbour] = Node(neighbour.val,[])
                    Q.append(neighbour)
                visited[curr_node].neighbors.append(visited[neighbour])                 # Appending visited[neighbour] and not just neighbour because we have to append cloned neighbours to the cloned nodes and visited[neighbour] represents cloned neighbour(Because its the value of a dictionary and values are cloned nodes !)
        return visited[node] 


n1 = Node(1,[])
n2 = Node(2,[])
n3 = Node(3,[])
n4 = Node(4,[])
n1.neighbors.append(n2)
n1.neighbors.append(n4)
n2.neighbors.append(n1)
n2.neighbors.append(n3)
n3.neighbors.append(n2)
n3.neighbors.append(n4)
n4.neighbors.append(n1)
n4.neighbors.append(n3)

s = Solution()
s.cloneGraph(n1)
        