# Author - Anantvir Singh, reference:= Data Structures in C by Seymour Lipschutz
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_ptr = None         # maintain a current pointer
        self.size = 0
    
    def add_item_at_rear(self,item):
        if self.head == None:           # list initially empty ?
            newNode = ListNode(item)
            self.head = newNode         
            self.tail = newNode
            self.size += 1
        else:
            newNode = ListNode(item)
            self.tail.next = newNode
            self.tail = newNode
            self.size += 1
        return newNode

class Solution(object):
    """---------------------------------- Own Solution ---------------------------------------"""

    """All test cases passed (36 ms). Faster than 82 % python online submissions"""

    def reverseKGroup(self,head,k):
        prev_tail = ListNode(0)                     # Create a dummy Node with value 0
        prev_tail.next = head                       
        global_first = prev_tail                    # Return this in the end. Points to start of the list always
        curr = prev_tail.next                       # Curr points to head initially
        count = 0
        begin = prev_tail.next                      # For each k group, it records the begin Node, so that we know where to start reversing
        #prev_node
        while curr != None:                         # Do until we traverse the entire list
            count += 1
            curr = curr.next
            if count % k == 0:                      # If count is a multiple of k
                curr_tail = self.reverse2(begin,prev_tail,curr)         # Pass the sentinel nodes and the begin node to reverse them
                begin = curr_tail.next
                prev_tail = curr_tail
        return global_first.next

    """
    This function takes 2 sentinel nodes begin and end which cover the entire list we want to sort. Example if this list is
    1->2->3->4->5 and we want to sort 2,3,4 to be 4->3->2, then begin = 1 and end = 5, head = 1. This then returns last node
    in the sorted list which has been connected to the last sentinel(The connection of this sorted k group to the entire
    linked list is made inside this function). In this case it returns 2 because the sorted list is 4->3->2 and current tail
    of this sorted group is given by 2. This 2 has already been connected to next 5 inside the function
    """
    def reverse2(self,head,begin,end):
        prev = begin
        first = prev
        second = prev.next
        curr = head
        next = None
        while curr != end:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        """Connect the sorted k group to rest of the list. It connects tail of previous sorted k group"""
        first.next = prev           # Connect with previous sorted k group
        second.next = end           # Connect current sorted k group with the rest of the list. i.e connect to the element next to the tail of this sorted group
        return second

    """-------------------------------------------------------------------------------"""

    """--------------------- Leetcode Solution ------------------------------"""
    def reverseKGroup2(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy_node = ListNode(0)
        dummy_node.next = head
        begin = dummy_node
        r = head
        count = 0
        while r != None:
            count += 1
            if count % k == 0:
                end = r.next
                prev_last = self.reverse(begin,end)
                begin = prev_last
                r = begin.next
            else:
                r = r.next
        return dummy_node.next              # Starting point of the reversed list (this is the 2nd node)

    def reverse(self,begin,end):
        prev = begin
        next_node = None
        curr = begin.next
        first = curr
        while curr != end:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        begin.next = prev
        first.next = curr
        return first


lnkdlst = LinkedList()
# head = lnkdlst.add_item_at_rear(3)
# lnkdlst.add_item_at_rear(4)
# lnkdlst.add_item_at_rear(9)
# lnkdlst.add_item_at_rear(2)
# lnkdlst.add_item_at_rear(5)
# lnkdlst.add_item_at_rear(8)
# lnkdlst.add_item_at_rear(7)
# lnkdlst.add_item_at_rear(6)
# lnkdlst.add_item_at_rear(12)
# lnkdlst.add_item_at_rear(20)

head=lnkdlst.add_item_at_rear(1)
# lnkdlst.add_item_at_rear(2)
# lnkdlst.add_item_at_rear(3)
# lnkdlst.add_item_at_rear(4)
# lnkdlst.add_item_at_rear(5)
s = Solution()
s.reverseKGroup2(head,2)
