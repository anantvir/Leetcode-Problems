"""
MAIN IDEA --> Idea is simple. Maintain a dictionary
visited ={

    Original Node : Cloned Node

}
Start iterating the list from the beginning until the current pointer is None. Intially insert the head into the visited
dictionary to start the process. Then proceed till the current node is None. If the next node of the current pointer exists
in the visited dict, then assign it to the next pointer of clone of current node. Else clreate the next node is visited
dict and then assign it to the next pointer of the clone of the current node. Repeat the same for the random pointer of the
current node also. If it exists, then assign to the random pointer of the current node. Else create it and then assign to the 
random pointer of the clone of current node

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        curr = head
        visited = dict()
        clonedHead = Node(head.val)
        visited[head] = clonedHead
        dummyHead = visited[head]
        while curr != None:

            """---------- Check if curr.next exists in visited. Assign to clone of curr if its exists, else create and then assign -------"""
            if curr.next:
                if curr.next in visited:
                    # If curr.next exists in visited, then assign it to clone of current
                    visited[curr].next = visited[curr.next]
                else:
                    # Else create it and then assign it to clone of curr
                    newNode = Node(curr.next.val)           # Clone
                    visited[curr.next] = newNode
                    visited[curr].next = visited[curr.next]
            
            """---------- Check if curr.random exists in visited. Assign to clone of curr if its exists, else create and then assign -------"""
            if curr.random:
                if curr.random in visited:
                    # If curr.random exists in visited, then assign it to clone of current
                    visited[curr].random = visited[curr.random]
                else:
                    # Else create it and then assign it to clone of curr
                    newNode = Node(curr.random.val)
                    visited[curr.random] = newNode
                    visited[curr].random = visited[curr.random]
            
            curr = curr.next
        
        return dummyHead

a = Node(7)
b = Node(13)
c = Node(11)
d = Node(10)
e = Node(1)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = None
a.random = None
b.random = a
c.random = e
d.random = c
e.random = a

s =Solution()
s.copyRandomList(a)

        