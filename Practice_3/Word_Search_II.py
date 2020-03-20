class Solution(object):
    class TrieNode:
        def __init__(self):
            self.children = dict()
            self.endOfWord = False
    def __init__(self):
        self.root = Solution.TrieNode()
        self.global_list = []
    
    def insert_in_trie(self,word):
        curr = self.root
        for i in range(len(word)):
            if word[i] in curr.children:
                curr = curr.children[word[i]]
            else:
                newNode = Solution.TrieNode()
                curr.children[word[i]] = newNode
                curr = curr.children[word[i]]
        curr.children['EOW'] = word
        curr.endOfWord = True

    def findWords(self, grid, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        def build_trie(grid,words):
            for word in words:
                self.insert_in_trie(word)
        build_trie(grid,words)
        nr = len(grid)
        nc = len(grid[0])
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] in self.root.children:
                    self.backtracking(grid,self.root,r,c)
        return self.global_list
    
    def backtracking(self,grid,prev_node,r,c):
        curr = prev_node.children[grid[r][c]]
        word = curr.children.pop("EOW",False)
        if word:
            self.global_list.append(word)  
        letter = grid[r][c]
        grid[r][c] = 'V'                                # mark visited
        nr = len(grid)
        nc = len(grid[0])
        for nbr_r,nbr_c in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
            if nbr_r < 0 or nbr_r > nr-1 or nbr_c < 0 or nbr_c > nc-1:
                continue
            if not grid[nbr_r][nbr_c] in curr.children:
                continue
            self.backtracking(grid,curr,nbr_r,nbr_c)
        grid[r][c] = letter                             # Restore the character where we marked visited

grid = [["a","a"]]
words = ["a"]

#words = ["oath","pea","eat","rain"]
s = Solution()
print(s.findWords(grid,words))

