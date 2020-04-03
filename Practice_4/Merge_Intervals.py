"""Sort the intervals by start time. Inset 1st interval into a new list. Start iterating from 2nd interval. If start of current
interval is <= last appended interval in newlist, then update the last interval in new list as 
max(current intervals end,new lists last intervals end). Example for input = [[1,4],[2,3]] newlist = [[1,4]], now
[2,3] will not be merged because end time of [2,3] i.e 3 is less than newlist[-1] """

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x:x[0])
        if len(intervals) == 0:
            return []
        new_lst = []
        new_lst.append(intervals[0])
        for i in range(1,len(intervals)):
            if intervals[i][0] <= new_lst[-1][1]:
                new_lst[-1][1] = max(intervals[i][1],new_lst[-1][1])
            else:
                new_lst.append(intervals[i])
        return new_lst

inp = [[1,4],[2,3]]

s = Solution()
print(s.merge(inp))