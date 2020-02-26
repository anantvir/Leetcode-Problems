"""
MAIN IDEA --> Store the next() value in contructor always. Whenever we call peek() just return the next stored value.
The next stored value will be updated when we call the next() method. When next() is called , then If self._next already exists,
means it is not None, then return self._next and make self._next = None. 
Now again set the value of self._next to next element of the iterator if next exists
"""

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._next = iterator.next()
        self._iterator = iterator
        
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._next
        
    def next(self):
        """
        :rtype: int
        """
        if self._next is None:
            raise StopIteration()

        to_return = self._next
        self._next = None
        if self._iterator.hasNext():
            self._next = self._iterator.next()
        return to_return

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._next is not None
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].