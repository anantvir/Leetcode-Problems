"""----------------------------Implementation of priority queue data structure--------------------------"""

class PriorityQueue:
    class Node:
        def __init__(self,info,priority):
            self.info = info
            self.priority = priority
            self.forward_link = None
    def __init__(self):
        self.head = None
        self.current_ptr = None
        self.previous = None
        self.size = 0

    def insert(self,info,priority):
        if self.head == None:
            newnode = self.Node(info,priority)
            self.head = newnode
            self.size += 1
        else:
            newnode = self.Node(info,priority)
            self.current_ptr = self.head
            while self.current_ptr.priority <= priority:
                self.previous = self.current_ptr
                self.current_ptr = self.current_ptr.forward_link
                if self.current_ptr == None:
                    self.previous.forward_link = newnode
                    self.size += 1
                    return newnode
            if self.current_ptr == self.head:
                newnode.forward_link = self.current_ptr
                self.head = newnode
                self.size += 1
            else:
                self.previous.forward_link = newnode
                newnode.forward_link = self.current_ptr
                self.size += 1
        return newnode
    
    def delete(self):
        if self.head == None:
            raise ValueError("Queue is Empty. Cannot remove an item !")
        else:
            removed_node = self.head                                    # Remove node
            print('Value of removed node is :',removed_node.info)       # Process removed node's data
            self.head = self.head.forward_link
            removed_node.forward_link = None
            
