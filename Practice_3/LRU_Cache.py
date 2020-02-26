class ListNode:
    def __init__(self,key,val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

"""MAIN IDEA --> Create 2 dummy nodes, head and tail. Seperate head and tail nodes are required to make insertions
even in empty list, easy
Use a doubly linked list to store key,val in each node and a hashmap {key : DLinkedList(key,value)}
Always insert new item on at the head of a doubly linked list. Whenever there is a get() command, move that item which we
are getting to the start of the doubly linked list.
Create separate functions for
1) adding node at head of doubly linked list
2) removing node from doubly linked list
3) removing the tail of doubly linked list
4) moving a given node to the head of the doubly linked list
"""
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.node_dict = dict()                     # Dictionary to store key : ListNode(key,value)
        self.capacity = capacity
        self.size = 0
        self.head = ListNode(0)                     # Create separate head and tail nodes so that even if we are inserting at beginning, we dont need to check null condition
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert_at_head(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def remove_node(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node
    
    def remove_tail(self):
        node = self.tail.prev
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        return node
    
    def move_to_head(self,node):
        self.remove_node(node)
        self.insert_at_head(node)

    """If node does not exist in node_dict, then return -1, else get the node and return its value
    Also, do not forget to move the node to the head of the doubly linked list
    """
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.node_dict.get(key,None)
        if node == None:
            return -1
        else:
            self.move_to_head(node)
            return node.val

    """If the node already exists, then modify its value and move it to the head of the doubly linked list, else create a new 
    node, insert it at the head, increment the size of doubly linked list, add it to node_dict, check if current size of doubly 
    linked list is greater than capacity. If yes, then delete the tail of the doubly linked list"""
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.node_dict.get(key,None)
        if node == None:
            newNode = ListNode(key,value)
            self.insert_at_head(newNode)
            self.size += 1
            self.node_dict[key] = newNode
            if self.size > self.capacity:
                tail = self.remove_tail()
                del self.node_dict[tail.key]
                self.size -= 1
        else:
            node.val = value
            self.move_to_head(node)


s = LRUCache(2)
s.put(1,1)
s.put(2,2)
print(s.get(1))
s.put(3,3)
print(s.get(2))
s.put(4,4)
print(s.get(1))
print(s.get(3))
print(s.get(4))