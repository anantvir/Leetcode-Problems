class Solution(object):

    """------------------ Better Brute Force (Store {element : index} hashmap for nums2 to make lookup O(1))------------------------"""
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        index_map = dict()              
        for k,v in enumerate(nums2):
            index_map[v] = k
        res = []
        for i in range(len(nums1)):
            idx = index_map[nums1[i]]
            for j in range(idx+1,len(nums2)):
                if nums2[j] > nums1[i]:
                    res.append(nums2[j])
                    break
            if j == len(nums2)-1 or idx == len(nums2)-1:
                res.append(-1)
        return res

nums1 = [4,1,2]
nums2 = [1,3,4,2]
s = Solution()
print(s.nextGreaterElement(nums1,nums2))
