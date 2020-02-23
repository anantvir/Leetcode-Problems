

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        i = l1
        j = l2
        dummyHead = ListNode(0)
        prev_node = dummyHead
        while i != None or j != None:
            x = i.val if i != None else 0
            y = j.val if j != None else 0
            sum = x + y + carry
            carry = sum // 10
            num = sum % 10
            num_Node = ListNode(num)
            prev_node.next = num_Node
            prev_node = num_Node
            i = i.next if i != None else None
            j = j.next if j != None else None
        if carry == 1:
            newNode = ListNode(carry)
            prev_node.next = newNode
        return dummyHead.next

l1 = ListNode(1)
l1.next = ListNode(8)
#l1.next.next = ListNode(3)

l2 = ListNode(0)
#l2.next = ListNode(6)
#l2.next.next = ListNode(4)

s = Solution()
s.addTwoNumbers(l1,l2)
        