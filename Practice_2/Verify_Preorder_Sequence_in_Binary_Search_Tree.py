class Solution(object):
    """---------------------------- Brute Force ---------------------------------"""
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        def isPreorder(arr,low,high):
            if low >= high:
                return True
            root = arr[low]
            i = low + 1
            while i <= high and arr[i] < root:
                i += 1
            j = i
            while j <= high and arr[j] > root:
                j += 1
            if j <= high:
                return False
            return isPreorder(arr,low+1,i-1) and isPreorder(arr,i,high)
        return isPreorder(preorder,0,len(preorder)-1)
    
    """----------------------------------- Efficient --------------------------------"""
    """
    Main Idea --> Keep pushing onto the stack unless the current element in preorder array is greater than the stack top.
    If current element is greater than stack top, then pop an element of stack and make it as lower. Keep popping the stack top
    till the current element is greater than the stack and keep assigning it to lower. We are basically finding the lower boundary
    for the next elements to come in the array. Because once we are in the right subtree, any value we will encounter, will be
    greater than the predecessor of that right value. Hence the predecessor will be the lower limit. Whenever we encounter a
    right child, we reassign the lower value. How will we find the predecessor ? --> Whenever we will get a value higher
    than stack top, it means we encountered a right child, We now need its predecessor to set it as lower limit. To find
    the predecessor, keep popping from stack until current element is smaller than stack top. The last popped item will be the 
    predecessor.
    """
    def verifyPreorder_Optimized(self,preorder):
        stack = []
        lower = float("-inf")
        for elem in preorder:
            if elem < lower:
                return False
            while stack and elem > stack[-1]:
                lower = stack.pop()
            stack.append(elem)
        return True

s = Solution()
print(s.verifyPreorder_Optimized([5,2,1,3,6]))
