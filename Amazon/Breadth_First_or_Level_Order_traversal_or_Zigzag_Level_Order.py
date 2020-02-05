import collections

# constant length implementation

class Queue_List:
    DEFAULT_CAPACITY = 15

    def __init__(self):
        self.Q = [None] * Queue_List.DEFAULT_CAPACITY   
        self.n = 0                                      # keep track of current number of elements in the queue. This variable will eb helpful in creating dynamic array implementation
        self.front = None                               # pointer for front of list
        self.rear = None                                #pointer for rear of list
    
    def isEmpty(self):
        return self.n == 0

    def enqueue(self,item):

        if self.front==0 and self.rear == len(self.Q) - 1:
            print('Overflow')
        
        #------------find new rear-----------
        if self.rear == len(self.Q) - 1:
            self.rear = 0
        elif self.front == None:
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1
        #--------------------------------------
        self.Q[self.rear] = item
        self.n += 1
        
        return self.Q

    def dequeue(self):
        if self.front == None:
            print('Underflow !')
        item = self.Q[self.front]
        self.Q[self.front] = None
        self.n -= 1
        #------------Find new front--------
        if self.front == self.rear:
            self.front = None
            self.rear = None
        elif self.front == len(self.Q) - 1:
            self.front = 0
        else:
            self.front += 1
        return item


class LinkedBinarySearchTree:
    class Node:
        def __init__(self,info):
            self.info = info
            self.left_child = None
            self.right_child = None
            self.parent = None
    def __init__(self):
        self.CURR_PTR = None
        self.size = 0
        self.root = None
    
    def find_item(self,item):
        """Using 2 variables, LOC = To store location of found item, PARENT = To store parent of LOC, SAVE = to
        store parent of CURR_PTR"""
        if self.root == None:
            LOC = None
            SAVE = None
            PARENT = None
            return LOC,PARENT
        if self.root.info == item:
            LOC = self.root
            PARENT = None
            return LOC,PARENT
        self.CURR_PTR = self.root
        if item < self.root.info:
            self.CURR_PTR = self.CURR_PTR.left_child
            SAVE = self.root
        else:
            self.CURR_PTR = self.CURR_PTR.right_child
            SAVE = self.root
        while self.CURR_PTR != None:
            if item == self.CURR_PTR.info:
                LOC = self.CURR_PTR
                PARENT = SAVE
                return LOC,PARENT
            elif item < self.CURR_PTR.info:
                SAVE = self.CURR_PTR
                self.CURR_PTR = self.CURR_PTR.left_child
            else:
                SAVE = self.CURR_PTR
                self.CURR_PTR = self.CURR_PTR.right_child
        LOC = None
        PARENT = SAVE
        return LOC,PARENT

    def insert_item(self,item):
        LOC,PARENT = self.find_item(item)
        if LOC != None:
            raise ValueError("Item already exists !")
        newNode = self.Node(item)
        if PARENT == None:
            self.root = newNode
        elif item < PARENT.info:
            PARENT.left_child = newNode
        else:
            PARENT.right_child = newNode
        print("New Node inserted successfully !")
        return newNode

    def delete_item_with_1_or_0_child(self,LOCATION,PARENT):

        if LOCATION.left_child == None and LOCATION.right_child == None:
            CHILD = None
        elif LOCATION.left_child != None and LOCATION.right_child == None:
            CHILD = LOCATION.left_child
        else:
            CHILD = LOCATION.right_child
        if PARENT != None:
            if LOCATION == PARENT.right_child:
                PARENT.right_child = CHILD
            else:
                PARENT.left_child = CHILD
        else:
            self.root = CHILD
        print("Deleted the node successfully !")
    
    def delete_item_with_2_children(self,LOCATION,PARENT):

        """Determine inorder successor SUC and parent of SUC i.e PARSUC"""
        PTR = LOCATION.right_child
        SAVE = LOCATION
        while PTR.left_child != None:
            SAVE = PTR
            PTR = PTR.left_child
        SUC = PTR
        PARSUC = SAVE

        """Delete inorder successor SUC"""
        self.delete_item_with_1_or_0_child(SUC,PARSUC)

        """Replace LOC by its inorder successor"""
        if PARENT != None:
            if LOCATION == PARENT.left_child:
                PARENT.left_child = SUC
            else:
                PARENT.right_child = SUC
        else:
            self.root = SUC
        
        """Assign left and right children of the newly added node the left and right children of the deleted node"""
        SUC.left_child = LOCATION.left_child
        SUC.right_child = LOCATION.right_child
        
        print("Deleted the node successfully !")

    def delete(self,item):
        LOC,PARENT = self.find_item(item)
        if LOC == None:
            raise ValueError("Item not in tree !")
        if LOC.left_child != None and LOC.right_child != None:
            self.delete_item_with_2_children(LOC,PARENT)
        else:
            self.delete_item_with_1_or_0_child(LOC,PARENT)
        print("Delete function completed !")
    
    def children(self,p):
        children_list = []
        if p.left_child != None and p.right_child != None:
            children_list.append(p.left_child)
            children_list.append(p.right_child)
        elif p.left_child != None and p.right_child == None:
            children_list.append(p.left_child)
        elif p.right_child != None and p.left_child == None:
            children_list.append(p.right_child)
        return children_list

    def breadth_first(self):
        Q = Queue_List()
        Q.enqueue(self.root)
        output_list = []
        while not Q.isEmpty():
            p = Q.dequeue()
            output_list.append(p.info)
            for child in self.children(p):
                Q.enqueue(child)
        return output_list

    def zig_zag_level_order_traversal(self):

        """Main idea is use 1 dequeue to store nodes and its children which will always be used
        like a normal queue i.e FIFO, and use 1 dequeue to store traversed nodes for each level FILO
        i.e if start_from_left = True then append at tail of dequeue, if start_from_left = False, 
        then append at head of dequeue. This dequeue will be renewed at each level"""

        output_list = []                                    # for final result
        level_list = collections.deque()                    # for nodes at each level. Depending on value of flag 'start_from_left', we either add elements from left(FILO) of dequeue or right of dequeue(FIFO)
        nodes_list = collections.deque([self.root,None])    # Store nodes and always pop them from left of queue and process them
        start_from_left = True
        while len(nodes_list) > 0:
            curr_node = nodes_list.popleft()
            if curr_node != None:
                if start_from_left == True:
                    level_list.append(curr_node.info)
                else:
                    level_list.appendleft(curr_node.info)
                if curr_node.left_child != None:
                    nodes_list.append(curr_node.left_child)
                if curr_node.right_child != None:
                    nodes_list.append(curr_node.right_child)         
            else:
                """If current popped node is None, it means one level completed"""
                output_list.append(level_list)          # Append level list to output list
                level_list = collections.deque()        # Recreate level list for next level
                if len(nodes_list) > 0:
                    nodes_list.append(None)             # Add delimiter for this level to mark the level
                start_from_left = not start_from_left   # Order will be reversed in each level 
        return output_list

t = LinkedBinarySearchTree()

t.insert_item(60)
t.insert_item(25)
t.insert_item(15)
t.insert_item(50)
t.insert_item(33)
t.insert_item(44)
t.insert_item(75)
t.insert_item(66)

print(t.zig_zag_level_order_traversal())
print('Finished !')
            

