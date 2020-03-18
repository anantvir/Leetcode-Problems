class Solution(object):
    def exist(self, grid, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        nr = len(grid)
        nc = len(grid[0])
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == word[0]:
                    found = self.dfs(grid,r,c,0,word)
                    if found == True:
                        return True
        return False
                    
    def dfs(self,grid,r,c,idx,word):
        if idx == len(word):
            return True
        nr,nc = len(grid),len(grid[0])
        if r < 0 or r > nr-1 or c < 0 or c > nc-1 or grid[r][c] == 'V' or grid[r][c] != word[idx]:
            return False
        temp = grid[r][c]
        grid[r][c] = 'V'
        found = self.dfs(grid,r+1,c,idx+1,word) or self.dfs(grid,r-1,c,idx+1,word) or  self.dfs(grid,r,c+1,idx+1,word) or self.dfs(grid,r,c-1,idx+1,word)
        grid[r][c] = temp
        return found
    
grid = [
    ["C","A","A"],
    ["A","A","A"],
    ["B","C","D"]]

s = Solution()
print(s.exist(grid,'AAB'))
