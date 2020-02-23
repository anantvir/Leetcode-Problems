"""------------------ Mai Idea --------------------------
distance --> This amtrix holds the total distance of that 0 from all the buildings(It increases everytime a new BFS runs as BFS appends to already existing distance)
reachable --> This matrix stores whether the 0 at (i,j) can reach all the buildings or not. Its maximum value at (i,j) can be total number of buildings in the grid i.e total number of ones !
visitied --> During the current BFS has this cell been visited or not

Scan the 2D grid, whenever you encounter a 1 i.e a building start a BFS. For each 0 you encounter
during the BFS, append its distance from the root node(1 from where BFS started) into the distance matrix
Run the BFS for all the buildings in the given grid each time appending to the distance matrix.
At the end distance(i,j) will contain sum of distances of (i,j) from all the buildings(ones) in the grid
At the end go through the entire matrix and choose the minimum value. Also check the reachable matrix to see if there is some 0
which has reachable(i,j) < total no. of buildings. If yes then return -1 else return the shortest distance
"""

from collections import deque
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        distance = [[0 for i in range(cols)]for i in range(rows)]
        reachable = [[0 for i in range(cols)]for i in range(rows)]      # Here index r,c stores how many buildings can the 0 at (r,c) reach. Maximum value can be total number of buildings in the given grid
        number_of_buildings = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:                                 # If you get a 1, run a BFS and increment toal no. of buildings
                    number_of_buildings += 1
                    self.BFS(r,c,grid,distance,reachable)

        shortest = float("inf")
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and reachable[i][j] == number_of_buildings:      # Scan through grid at the end and return shortest distance if that cell satisfies the given constraints
                    shortest = min(shortest,distance[i][j])
        if shortest == float("inf"):
            return -1
        else:
            return shortest             

    def BFS(self,r,c,grid,distance,reachable):
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for i in range(cols)]for i in range(rows)]            # Visited 2d grid declared inside BFS because its created fresh for each BFS traversal and erased at the end
        queue.append((r,c,0))                                               # Intially to start BFS append root node into queue with distance = 0
        while queue:
            curr_r,curr_c,curr_dist = queue.popleft()
            for nb in [(curr_r+1,curr_c),(curr_r-1,curr_c),(curr_r,curr_c+1),(curr_r,curr_c-1)]:    # left,right,up,down neighbours of current cell
                nb_row = nb[0]                                              # nb means neighbour, nb_row/nb_col
                nb_col = nb[1]
                if 0 <= nb_row <= rows-1 and 0 <= nb_col <= cols-1 and grid[nb_row][nb_col] == 0 and visited[nb_row][nb_col] != 'Visited':
                    distance[nb_row][nb_col] += curr_dist + 1
                    visited[nb_row][nb_col] = 'Visited'
                    reachable[nb_row][nb_col] += 1
                    queue.append((nb_row,nb_col,curr_dist+1))
        

grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
s = Solution()
print(s.shortestDistance(grid))

