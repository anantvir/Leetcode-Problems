class Solution(object):
    """Simulate the problem. Find a cycle or period.
    Compute next state each time and see if its in hashset, it no then add it to hashset. If it does exist, then N = N % size. That will give the index
    we need to find in the period. Run the nextState() function for those number until that index is reached and return the final value"""
    def prisonAfterNDays2(self,cells,N):
        hashset = set()
        size = 0
        flag = False
        for i in range(N):
            nextDayValue = self.nextState(cells)
            if tuple(nextDayValue) not in hashset:
                hashset.add(tuple(nextDayValue))
                size += 1
            else:
                flag = True
                break
            cells = nextDayValue
        if flag:
            N = N % size
            for i in range(1,N+1):
                cells = self.nextState(cells)
        return cells

    def nextState(self,cells):
        curr = [0]*len(cells)
        for i in range(1,len(cells)-1):
            if cells[i-1] == cells[i+1]:
                curr[i] = 1
        return curr
    
cells = [0,1,0,1,1,0,0,1]
N = 7
s = Solution()
print(s.prisonAfterNDays2(cells,N))                