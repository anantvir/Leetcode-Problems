import math

class LinkedList:
    class Node:
        def __init__(self,info):
            self.info = info
            self.forward_link = None
    
    def __init__(self):
        self.current_ptr = None
        self.size = 0
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.size == 0
    
    def insert_at_rear(self,info):
        if self.head is None:
            new_node = self.Node(info)
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node = self.Node(info)
            self.tail.forward_link = new_node
            self.tail = new_node
            self.size += 1
        return new_node



ll1 = LinkedList()
ll1.insert_at_rear(7)
ll1.insert_at_rear(8)
#ll1.insert_at_rear(3)

ll2 = LinkedList()
ll2.insert_at_rear(7)
ll2.insert_at_rear(9)
#ll2.insert_at_rear(4)  


"""Just add elements of two lists like normal arithematic addition"""
def add_lists(ll1,ll2):
    carry = 0
    x = ll1.head
    y = ll2.head
    new_list = LinkedList()
    while(x != None or y != None or carry != 0):
        if x == None and y == None and carry != 0:
            new_list.insert_at_rear(carry)
        else:
            total = x.info + y.info + carry
            carry = math.floor(total/10)
            info = total % 10
            new_list.insert_at_rear(info)
            x = x.forward_link
            y = y.forward_link
    return new_list

add_lists(ll1,ll2)
    
