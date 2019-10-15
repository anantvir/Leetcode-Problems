"""Author - Anantvir Singh, Problem Source - Leetcode, Statement - Merge K Sorted Lists"""

class Node:
    def __init__(self,info,link= None):
        self.info = info
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_ptr = None         # maintain a current pointer
        self.size = 0
    
    def get_head(self):
        return self.head

    def add_item_at_rear(self,item):
        if self.head == None:           # list initially empty ?
            newNode = Node(item)
            self.head = newNode         
            self.tail = newNode
            self.size += 1
        else:
            newNode = Node(item)
            self.tail.link = newNode
            self.tail = newNode
            self.size += 1
        return newNode
    
    def add_item_at_front(self,item):
        if self.head == None:
            newNode = Node(item)
            self.head = newNode
            self.tail = newNode
            self.current_ptr = newNode
            self.size += 1
        else:
            newNode = Node(item)
            newNode.link = self.head
            self.head = newNode
            self.size += 1
        return newNode

    def traverse_linked_list(self):
        temp_list =[]
        if self.current_ptr == None:
            self.current_ptr = self.head                #initialize current pointer to start/head of list
        while self.current_ptr != None:                 # while last item with link = Null/None is not reached
            temp_list.append(self.current_ptr.info)     #process the item
            self.current_ptr = self.current_ptr.link    #increment the pointer
        return temp_list

llst = []

l1 = LinkedList()
l1.add_item_at_rear(1)
l1.add_item_at_rear(4)
l1.add_item_at_rear(5)
llst.append(l1)

l2 = LinkedList()
l2.add_item_at_rear(1)
l2.add_item_at_rear(3)
l2.add_item_at_rear(4)
llst.append(l2)

l3 = LinkedList()
l3.add_item_at_rear(2)
l3.add_item_at_rear(6)
llst.append(l3)

"""Maintain 2 pointers i and j to heads of both lists. """

def MergeTwoSortedLists(l1,l2): 
    i = l1.get_head()
    j = l2.get_head()
    result = LinkedList()
    while(i != None or j != None):      # Will run until both pointers are Null
        if i == None:                   # If i is Null that means i linked list is finished. Now no need for comparisions, just add elements of j list to result
            item = j.info
            result.add_item_at_rear(item)
            j = j.link
        elif j == None:                 # If j is Null that means j linked list is finished. Now no need for comparisions, just add elements of i list to result
            item = i.info
            result.add_item_at_rear(item)
            i = i.link
        else:                           # If both are not null
            if i.info <= j.info:        # Compare elements, add lesser one to result and increment the pointer of list containing the lesser value node
                result.add_item_at_rear(i.info)
                i = i.link
            else:
                result.add_item_at_rear(j.info)
                j = j.link
    return result


"""Main Idea is call MergeTwoSortedLists() again and again. Maintain 2 pointers called result which initially refers to 1st element
in the llst and j which initially refers to 2nd element in llst.
During each iteration of for loop, result and j value are passed to MergeTwoSortedLists(). Its result is again stored in result
and j is incremented by 1
Write this on paper to understand better"""

def Merge_k_SortedLists(llst):      
    result = llst[0]        # Set result variable as 1st element of llst (list of linked lists)
    j = 1                   # j refers to 2nd element of llst initially
    for p in range(len(llst)-1):        # if size of llst = 3 the p = 1 to 2 because i refers to 2nd element in llst and j refers to 3rd element in llst
        result = MergeTwoSortedLists(result,llst[j])        # call MergeTwoSortedLists repeatedly
        j += 1
    return result

Merge_k_SortedLists(llst)