from collections import defaultdict

class TrieNode:
        def __init__(self):
            self.children = defaultdict(TrieNode)
            self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    """-------------------------------- Insert(Interative) ---------------------------------------"""
    def insert_iterative(self,word):
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                newTrieNode = TrieNode()
                curr.children[word[i]] = newTrieNode
            curr = curr.children[word[i]]
        """ Mark the end of word = True when we reach the last character of input word"""
        curr.endOfWord = True
    
    """-------------------------------- Insert(Recursive) -----------------------------------------"""
    def insert_recursive(self,word,idx,curr):
        if idx == len(word):
            curr.endOfWord = True
            return
        newTrieNode = curr.children[word[idx]]
        if newTrieNode == None:
            newTrieNode = TrieNode()
            curr.children[word[idx]] = newTrieNode
        self.insert_recursive(word,idx+1,newTrieNode)

    """-------------------------------- Search (Iterative) ----------------------------------------"""
    def search_iterative(self,word):
        curr = self.root
        for i in range(len(word)):
            if word[i] in curr.children:
                curr = curr.children[word[i]]
            else:
                return False
        return curr.endOfWord
    
    """-------------------------------- Search (Recursive) ----------------------------------------"""
    def search_recursive(self,word,curr,idx):
        if idx == len(word):
            return curr.endOfWord
        curr = curr.children[word[idx]]
        if curr == None:
            return False
        return self.search_recursive(word,curr,idx+1)
    

t = Trie()
t.insert_recursive('abc',0,t.root)
t.insert_recursive('abgl',0,t.root)
t.insert_recursive('cdf',0,t.root)
t.insert_recursive('abcd',0,t.root)
t.insert_recursive('lmn',0,t.root)


print(t.search_iterative('abcd'))
