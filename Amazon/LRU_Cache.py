from collections import OrderedDict

"""----------------------- Approach 1(Lengthy and error prone) -------------------------"""
"""Create a dequeue and keep inserting at rear. Whenevr you get() an item, check if it already exists in the
dequeue. If yes remove that node and take it to tail of the dequeue. If dequeue(cache) is full, then remove the head
of the dequeue to make space"""
class Node:
    def __init__(self,key,value = None):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None
    
class LinkedListCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0
    
    def put(self,newNode):
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            self.size += 1
        else:
            """Search if node with key already exists in queue"""
            item = newNode.key
            removedNode = self.get(item)
            if removedNode == None:
                self.add_node_at_tail(newNode)
            if self.size > self.capacity:
                self.evict_head_node()
    
    def get(self,key):
        curr_ptr = self.tail
        while curr_ptr != None:
            if curr_ptr.key == key:
                removedNode = self.remove_node(curr_ptr)
                self.add_node_at_tail(removedNode)
                return removedNode
            curr_ptr = curr_ptr.previous
        return None

    def remove_node(self,node):
        if node == self.head:
            self.head = self.head.next
            node.next = None
            if self.head.previous:
                self.head.previous = None
            self.size -= 1
        elif node == self.tail:
            self.tail = self.tail.previous
            self.tail.next = None
            self.size -= 1
        else:
            node.previous.next = node.next
            node.next.previous = node.previous
            self.size -= 1
        return node
    
    def add_node_at_tail(self,node):
        if self.tail != None:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
            self.size += 1

    def evict_head_node(self):
        if self.head != None:
            self.head.previous = None
            self.head = self.head.next
            self.head.previous.next = None
            self.head.previous = None


# lru = LinkedListCache(5)
# lru.put(Node('F',10))
# lru.put(Node('C',5))
# lru.put(Node('E',11))
# lru.put(Node('B',13))
# lru.put(Node('A',21))
# print(lru.get('E'))
# print(lru.get('M'))
# lru.put(Node('D',49))

# lru = LinkedListCache(2)

# lru.put(Node(1,1))
# lru.put(Node(2,2))
# print('Get value with key 1 :',lru.get(1).value)
# lru.put(Node(3,3))
# print(lru.get(2))
# lru.put(Node(4,4))
# print(lru.get(1))
# print(lru.get(3))
# print(lru.get(4))

"""--------------------- Approach 2 (Using OrderedDict class in python)------------------------"""
"""OrderedDict class creates a dictionary which is constructed using a linked list. This dictionary maintains
order in which elements are inserted along with regular O(1) time operations of a normal dict. OrderedDict
contains following useful methods
move_to_end(node) --> Moves that node to the end of dictionary/linked list
popitem(last=False) --> if last = false then pops item in FIFO order(That is what we want. Item which came first in the queue
must be removed first as well from the queue. This is the rule of LRU cache), if last=True pops item in LIFO order"""

from collections import OrderedDict

class LRUCache(OrderedDict):
    def __init__(self,capacity):
        self.capacity = capacity
    
    def get(self,key):
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self,key,value):
        if key not in self:
            self[key] = value
        else:
            self.move_to_end(key)
            self[key] = value
            return self[key]
        if len(self) > self.capacity:
            self.popitem(last=False)
            print('Popped !')
    
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)    
print(cache.get(2))     
cache.put(4, 4)    
print(cache.get(1))   
print(cache.get(3))    
print(cache.get(4))



