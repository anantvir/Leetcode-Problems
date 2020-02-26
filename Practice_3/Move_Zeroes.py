"""
MAIN IDEA --> Keep 2 pointers. i points to current 0 element and j searches for first non zero element which comes after i.
As soon as we get a j, we swap i and j. So index i now becomes non zero. Now move i to next index i.e i+1 and now check if i 
is zero or non zero. If i is still zero, then again search for 1st non zero element represented by j and swap again.
If i is now non-zero then no need to swap we already have a non zero in the beginning of array, so we just move the pointer i forward
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 1
        n = len(nums)
        while j < n and i < j:                          # j searches for the 1st non zero element after pointer i
            if nums[i] == 0 and nums[j] != 0:           # If element at i is zero and j != 0, swap them
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
                j += 1
                continue
            if nums[i] != 0:                            # If i is not zero, then just increment both i and j
                i += 1
                #j += 1
                continue
            if nums[i] == 0 and nums[j] == 0:
                j += 1
                continue
        return nums

    
nums = [-959151711,623836953,209446690,-1950418142,1339915067,-733626417,481171539,-2125997010,-1225423476,1462109565,147434687,-1800073781,-1431212205,-450443973,50097298,753533734,-747189404,-2070885638,0,-1484353894,-340296594,-2133744570,619639811,-1626162038,669689561,0,112220218,502447212,-787793179,0,-726846372,-1611013491,204107194,1605165582,-566891128,2082852116,0,532995238,-1502590712,0,2136989777,-2031153343,371398938,-1907397429,342796391,609166045,-2007448660,-1096076344,-323570318,0,-2082980371,2129956379,-243553361,-1549960929,1502383415,0,-1394618779,694799815,78595689,-1439173023,-1416578800,685225786,-333502212,-1181308536,-380569313,772035354,0,-915266376,663709718,1443496021,-777017729,-883300731,-387828385,1907473488,-725483724,-972961871,-1255712537,383120918,1383877998,1722751914,0,-1156050682,1952527902,-560244497,1304305692,1173974542,-1313227247,-201476579,-298899493,-1828496581,-1724396350,1933643204,1531804925,1728655262,-955565449,0,-69843702,-461760848,268336768,1446130876]
s = Solution()
print(s.moveZeroes(nums))
            