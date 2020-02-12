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
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        next = None
        curr = head
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

ll = LinkedList()
head = ll.add_item_at_rear(3)
ll.add_item_at_rear(4)
ll.add_item_at_rear(9)

s = Solution()
s.reverseList(head)
        