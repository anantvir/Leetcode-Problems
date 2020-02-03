class Solution(object):
    """--------- Do what the question says -----------"""
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        prev = cells                        # Because we have to compare with the previous state of prisons
        for day in range(N):                # For N number of days
            curr = [0]*len(cells)           # For each day create a fresh list of prisons and at the end of day assign it to prev pointer
            for i in range(1,7):            # For days
                if prev[i-1] == 0 and prev[i+1] == 0 or prev[i-1] == 1 and prev[i+1] == 1:  # Check for given condition, both adjacent cells should either be occupied or vacant 
                    curr[i] = 1
                else:
                    curr[i] = 0
            """# IMPORTANT --> first and last cell will become 0 after 1st day and will remain zero afterwards. 
            Because cells on both sides should be empty or occupied for current cell to be occupied and 
            1st and last cells dont have 2 adjacent cells so we dont know what their state will be afterwards"""
            if day == 0:                    
                curr[0]=0           # At the end of 1st day make 1st and last cell 0
                curr[-1]=0
            prev = curr             # At the end of the current day, make current state as previous state
        return curr
                                
cells = [0,1,0,1,1,0,0,1]
s= Solution()
print(s.prisonAfterNDays(cells,7))
        