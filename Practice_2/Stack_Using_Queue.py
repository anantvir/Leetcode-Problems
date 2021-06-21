"""------------- Maintain 2 queues for the Pop operation--------------------"""

"""Pop takes O(n) time and push takes O(1) time. For pop operation, dequeu from Q1 until Q1's length == 1 and keep pushing
Q1's elements into Q2. Finally deque the last element from Q1 and return it !"""

from collections import deque
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Q1 = deque()
        self.Q2 = deque()
        
    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.Q1.append(x)                               # Enqueue Operation

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if len(self.Q2) == 0:
            while len(self.Q1) != 1:
                elem = self.Q1.popleft()
                self.Q2.append(elem)
        res = self.Q1.popleft()                         # Deque Operation
        temp = self.Q1
        self.Q1 = self.Q2
        self.Q2 = temp
        return res

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.Q1[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.Q1) == 0

s = MyStack()
s.push(5)
s.push(6)
s.push(7)
s.push(8)
s.push(9)
print(s.pop())

print(s.empty())