"""
Main IDEA --> Maintain 3 pointers, i,j for list 1 and list 2, and a previous pointer which points to
the last element in the resuting sorted list. Dont create any new node. Just modify pointers of
existing nodes
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i = l1
        j = l2
        first = ListNode(0)
        prev = first
        while i != None or j != None:
            if i == None and j != None:
                prev.next = j
                j = None
            elif j == None and i != None:
                prev.next = i
                i = None
            elif i.val == j.val:
                prev.next = i
                prev = i
                i = i.next
            elif i.val > j.val:
                prev.next = j
                prev = j
                j = j.next
            elif j.val > i.val:
                prev.next = i
                prev = i
                i = i.next
        return first.next

head1 = ListNode(1)
head1.next = ListNode(4)
head1.next.next = ListNode(5)
        
head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)

head3 = ListNode(2)
head3.next = ListNode(6)

list_of_ll = [head1,head2,head3]

s = Solution()
s.mergeTwoLists(head1,head2)
        