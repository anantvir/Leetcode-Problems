class Solution(object):
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
        
s = Solution()
print(s.verifyPreorder([5,2,1,3,6]))
