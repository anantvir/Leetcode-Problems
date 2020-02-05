s = list('ABCCED')
grid = [['1','1','1','1','1','1'],
['1','A','B','C','E','1'],
['1','S','F','C','S','1'],
['1','A','D','E','E','1'],
['1','1','1','1','1','1',]]


def WordSearch(grid,word):
  nr = len(grid)-2
  nc = len(grid[0])-2
  for r in range(1,nr):
    for c in range(1,nc):
        if grid[r][c] == word[0] and DFS(grid,r,c,0,word):
            return True
        else:
            False


def DFS(grid,r,c,count,word):
    if count == len(word):
        return True
    nr_index = len(grid)-3
    nc_index = len(grid[0])-3

    if r < 1 or c < 1 or r > nr_index+1 or c > nc_index+1 or grid[r][c] != word[count]:
        return False

    grid[r][c] = 'Visited'
    found = DFS(grid,r+1,c,count+1,word) or DFS(grid,r-1,c,count+1,word) or DFS(grid,r,c-1,count+1,word) or DFS(grid,r,c+1,count+1,word)

    return found

print(WordSearch(grid,s))