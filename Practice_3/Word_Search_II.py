class Solution(object):
    def findWords(self, grid, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        nr = len(grid)
        nc = len(grid[0])
        char_dict = dict()
        for word in words:
            char_dict[word[0]] = word
        global_set = set()
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] in char_dict:
                    print(char_dict[grid[r][c]])
                    found = self.dfs(grid,r,c,0,char_dict[grid[r][c]])
                    if found == True:
                        global_set.add(char_dict[grid[r][c]])
        if len(global_set) > 0:
            return list(global_set)
        else:
            return []

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

grid = [["a","b"],["c","d"]]
words = ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]
 
s = Solution()
print(s.findWords(grid,words))

