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

    

t = Trie()
t.insert_recursive('abc',0,t.root)
t.insert_recursive('abgl',0,t.root)
t.insert_recursive('cdf',0,t.root)
t.insert_recursive('abcd',0,t.root)
t.insert_recursive('lmn',0,t.root)