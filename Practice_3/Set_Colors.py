"""
MAIN IDEA --> This is well known problem called Dutch National Flag Problem proposed by Edsger Djikstra.
Use 3 pointers
i --> tracks right boundary of zeroes i.e all elements before(not including) this index will be zeroes
j --> tracks leftmost boundary of 2's i.e all elements after(not including) this index will be 2's
curr --> current element that is being tracked
while curr <= j:
    
    If nums[curr] = 0 : swap currth and i th elements and move both pointers to the right.

    If nums[curr] = 2 : swap currth and j th elements. Move pointer j to the left.

    If nums[curr] = 1 : move pointer curr to the right.

"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def swap(nums,i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        i = 0
        j = len(nums) - 1
        curr = 0
        while curr <= j:
            if nums[curr] == 2:
                swap(nums,curr,j)
                j -= 1
            elif nums[curr] == 0:
                swap(nums,curr,i)
                i += 1
                curr += 1
            else:
                curr += 1
        return nums
    
a = [2,0,2,1,1,0,1,0,2,0,1,0,2]
s = Solution()
print(s.sortColors(a))

        