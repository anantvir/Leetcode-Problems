class MinStack(object):

    """MAIN IDEA --> Push a tuple on the stack every time you push an element. The tuple is (element,min(element,stack[-1]))
    i.e check if the top of stack is less than current element. If yes then push (element,top of stack) else push (element,elemt)
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, elem):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) == 0:
            self.stack.append((elem,elem))
        else:
            if self.stack[-1][1] > elem:
                self.stack.append((elem,elem))
            else:
                self.stack.append((elem,self.stack[-1][1]))
        
    def pop(self):
        """
        :rtype: None
        """
        elem = self.stack.pop()
        return elem[0]    

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        
    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
        


minStack =MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())