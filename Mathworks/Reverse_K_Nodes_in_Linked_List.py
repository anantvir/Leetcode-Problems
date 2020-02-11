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
    def reverseKGroup(self, head, k):
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
