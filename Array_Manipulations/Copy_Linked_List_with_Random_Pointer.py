

class Node:
    def __init__(self,info,link= None,random = None):
        self.info = info
        self.link = link
        self.random = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_ptr = None         # maintain a current pointer
        self.size = 0
    
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

ll = LinkedList()
n1 = ll.add_item_at_rear(7)
n2 = ll.add_item_at_rear(13)
n3 = ll.add_item_at_rear(11)
n4 = ll.add_item_at_rear(10)
n5 = ll.add_item_at_rear(1)
n1.random = None
n2.random = n1
n3.random = n5
n4.random = n3
n5.random = n1  

input_list = [[7,None],[13,0],[11,4],[10,2],[1,0]]

"""-------------- Approach 1 (INEFFICIENT since it requires 2 passes over the given Linked List)-------------"""
class Solution1:
    def Copy_List(self,head):        
        curr_ptr = head
        new_ll = LinkedList()
        while curr_ptr != None:
            new_ll.add_item_at_rear(curr_ptr.info)
            curr_ptr = curr_ptr.link
        curr_old = head
        curr_new = new_ll.head
        while curr_old != None:
            curr_new.random = curr_old.random
            curr_old = curr_old.link
            curr_new = curr_new.link
        return new_ll

#s1 = Solution1()
#s1.Copy_List(n1)

"""------------------- Approach 2 from Leetcode Solution (EFFICIENT)-------------------"""
class Solution2:
    
    def __init__(self):
        self.visited_dict = {}

    def GetClonedNode(self,node):
        if node:
            if node in self.visited_dict:
                return self.visited_dict[node]
            else:
                new_Node = Node(node.info,None,None)
                self.visited_dict[node] = new_Node
                return self.visited_dict[node]
        else:
            return None
    
    def Copy_List_Approach_2(self,head):
        curr_ptr = head
        if head == None:
            return None
        new_Node = Node(curr_ptr.info,None,None)
        self.visited_dict[curr_ptr] = new_Node
        while curr_ptr != None:
            # Get clones of nodes referenced by next and random pointers
            # If they dont exist then GetClonedNode method inserts those nodes in visited dictionary
            new_Node.random = self.GetClonedNode(curr_ptr.random)
            new_Node.link = self.GetClonedNode(curr_ptr.link)

            # Move the pointers to next node
            curr_ptr = curr_ptr.link
            new_Node = new_Node.link
        return self.visited_dict[head]

    """--------------------- Approach 3 (Self) ---------------------------"""
    """Check if curr_ptr in visited dict, if yes then take the new node corresponding to that curr_ptr
    else create a new node. Then iterate over original list and everytime check if a new node exists
    corresponding to the old node(curr_ptr). If not then create one"""
    def Copy_List_Approach_3(self,head):
        curr_ptr = head

        while curr_ptr != None:
            if curr_ptr not in self.visited_dict:           # If current node does not exist in hashtable
                new_Node = Node(curr_ptr.info,None,None)    # create it and store in hashtable
                self.visited_dict[curr_ptr] = new_Node
            else:
                new_Node = self.visited_dict[curr_ptr]      # Else takt the existing node and make it new_node
            if curr_ptr.link:                               
                if curr_ptr.link in self.visited_dict:      # check if curr_ptr.link exists in hashtable
                    new_Node.link = self.visited_dict[curr_ptr.link]   # If yes then make it as link of new node
                else:
                    new_link_Node = Node(curr_ptr.link.info,None,None)  # if link of current pointer does not exist in hashtable then create one
                    self.visited_dict[curr_ptr.link] = new_link_Node    # Store the newly created link in hashtable
                    new_Node.link = self.visited_dict[curr_ptr.link]    # Set that link to be the link of new node
            else:
                new_Node.link = None
            
            if curr_ptr.random:                                         # Repeat the above steps for node corresponding to curr_ptr.random
                if curr_ptr.random in self.visited_dict:
                    new_Node.random = self.visited_dict[curr_ptr.random]
                else:
                    new_random_Node = Node(curr_ptr.random.info,None,None)
                    self.visited_dict[curr_ptr.random] = new_random_Node
                    new_Node.random = self.visited_dict[curr_ptr.random]
            else:
                new_Node.random = None
            curr_ptr = curr_ptr.link
        return self.visited_dict[head]
        
s2 = Solution2()
s2.Copy_List_Approach_3(n1)
            

        
    


    

