"""Author - Anantvir Singh, Problem Source - Leetcode, Statement - Add two numbers"""

"""The main part to pay attention is that there can be only 1 number in each node even in the output. So if Sum >= 10,
a carry will be generated which we have to take to next step of addition as we do in regular mathematics."""

class Node:
        def __init__(self,info = None,link = None):
            self.info = info
            self.link = link

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_ptr = None
        self.size = 0
    def get_size(self):
        return self.size
    def is_Empty(self):
        return self.size == 0
    
    def get_head(self):
        return self.head
    
    def get_tail(self):
        return self.tail

    def insert_at_rear(self,val):
        if self.is_Empty():
            newNode= Node(val)
            self.head = newNode
            self.tail = newNode
            self.size += 1
        else:
            newNode = Node(val)
            self.tail.link = newNode
            self.tail = newNode
        return newNode
    
    def insert_at_front(self,val):
        if self.is_Empty():
            newNode= Node(val)
            self.head = newNode
            self.tail = newNode
            self.size += 1
        else:
            newNode.link = self.head
            self.head = newNode
            self.size += 1
    
    def traverse_list(self):
        self.current_ptr = self.head
        lst = list()
        while (self.current_ptr != None):
            lst.append(self.current_ptr.info)
            self.current_ptr = self.current_ptr.link
        return lst

l1 = LinkedList()
l1.insert_at_rear(2)
l1.insert_at_rear(4)
l1.insert_at_rear(3)

l2 = LinkedList()
l2.insert_at_rear(5)
l2.insert_at_rear(6)
l2.insert_at_rear(4)
#l2.insert_at_rear(9)

def addTwoNumbers(l1,l2):
    h1 = l1.get_head()
    h2 = l2.get_head()
    carry = 0
    temp = 0
    result = LinkedList()
    while(h1 != None or h2 != None):                # 1 list can be longer than other, so end loop only when both have been iterated 
        p = h1.info if h1 != None else 0            # if one list is finished, then set p = 0 for that list
        q = h2.info if h2 != None else 0
        Sum = p + q + carry
        if Sum >= 10:                               # if sum>10 carry will be generated
            temp = Sum % 10
            carry = Sum//10                       #""" ---IMPORTANT---->>>Carry is calculated in both cases, if we dont then a non zero carry from previous iteration will again be added to sum i.e check in each case, if carry becomes zero, then set it to zero"""
        else:
            temp = Sum
            carry = Sum//10
        result.insert_at_rear(temp)
        h1 = h1.link if h1 != None else None        
        h2 = h2.link if h2 != None else None
    return result
