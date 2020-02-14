"""Main Idea --> You cannot use any operations other than native stack operations.
Like you cannot delete an element based on index etc. You only need to use push and pop etc.
i.e all operations native to a stack
Hence create 2 stacks. You can either make enqueue operation expensive and dequeue fast
or vice versa. 
I made dequeue expensive.

"""

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.primary_stack = []
        self.secondary_stack = []
        
    """Just append to the primary stack this acts ans queue as elements are added at the end"""
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.primary_stack.append(x)
    
    """To pop, first move all elements from primary to secondary stack. First check if secondary stack is empty.
    If is empty, then pop from primary and append to secondary until len(primary)==0
    Important point is to check if secondary stack i.e stack 2 is empty or not before transferring
    elements from primary to secondary"""
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.secondary_stack) == 0:
            while len(self.primary_stack) != 0:
                elem = self.primary_stack.pop()
                self.secondary_stack.append(elem)
        return self.secondary_stack.pop()
        
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.secondary_stack) != 0:
            return self.secondary_stack[-1]
        else:
            return self.primary_stack[0]
        
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.primary_stack) == 0 and len(self.secondary_stack) == 0:
            return True
        else:
            return False

q = MyQueue()
q.push(5)
q.push(6)
q.push(7)
q.push(8)
print(q.peek())
print(q.pop())
q.pop()
q.pop()
q.pop()
print(q.empty())
