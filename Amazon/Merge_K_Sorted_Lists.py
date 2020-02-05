"""
Use Merge 2 sorted lists k-1 times. For Merge Two Sorted Lists refer to bellow comment

Keep 2 pointers to track if any of the 2 lists is finished (While loop). For each pointer, compare which element
is greater and append at rear of new list. If one list is finished, just append the other list to the end of new list"""

class LinkedList:
    class Node:
        def __init__(self,info):
            self.info = info
            self.forward_link = None
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_ptr = None
        self.size = 0
    def insert_at_rear(self,info):
        if self.head == None:
            newnode = self.Node(info)
            self.head = newnode
            self.tail = newnode
            self.size += 1
        else:
            newnode = self.Node(info)
            self.tail.forward_link = newnode
            self.tail = newnode
            self.size += 1
        return newnode

ll1 = LinkedList()
ll1.insert_at_rear(1)
ll1.insert_at_rear(2)
ll1.insert_at_rear(4)
ll1.insert_at_rear(5)
ll1.insert_at_rear(8)
ll1.insert_at_rear(9)
        
ll2 = LinkedList()
ll2.insert_at_rear(1)
ll2.insert_at_rear(3)
ll2.insert_at_rear(4)

ll3 = LinkedList()
ll3.insert_at_rear(1)
ll3.insert_at_rear(2)
ll3.insert_at_rear(2)
ll3.insert_at_rear(5)

list_of_lists = [ll1,ll2,ll3]

def Merge_Two_lists(l1,l2):
    new_list = LinkedList()
    i = l1.head
    j = l2.head
    while(i != None or j != None):
        if i == None and j != None:
            while j != None:
                new_list.insert_at_rear(j.info)
                j = j.forward_link
            return new_list
        if j == None and i != None:
            while i != None:
                new_list.insert_at_rear(i.info)
                i = i.forward_link
            return new_list
        if i.info <= j.info:
            new_list.insert_at_rear(i.info)
            i = i.forward_link
        else:
            new_list.insert_at_rear(j.info)
            j = j.forward_link
    return new_list

def Merge_K_Sorted_Lists(lst):
    prev = Merge_Two_lists(lst[0],lst[1])       # first merge top 2 lists and store the o/p list in a variable
    for i in range(2,len(lst)):                 # start from 3rd linked list in array of linked lists i.e index 2 to last linked list, pass previous and current i th Linked List
        prev = Merge_Two_lists(prev,lst[i])

Merge_K_Sorted_Lists(list_of_lists)
