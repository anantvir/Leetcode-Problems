"""---------- Approach 1 Brute Force -----------------"""

"""Store the move in matrix and 
Check the row i and column j and both diagnols for evry move"""

class TicTacToe(object):

    def __init__(self, n):
        """Initialize your data structure here."""
        self.n = n
        self.m = [[0 for i in range(self.n)]for i in range(self.n)]
        
    def move(self, i, j, player):
        count_row = 0
        count_column = 0
        count_left_diag = 0
        count_right_diag = 0
        player_code = {1:'X',2:'O'}
        self.m[i][j] = player_code[player]
        for k in range(self.n):
            if self.m[k][j] == player_code[player]:
                count_column += 1
            if self.m[i][k] == player_code[player]:
                count_row += 1
            if self.m[k][k] == player_code[player]:
                count_left_diag += 1
            if self.m[self.n-1-k][k] == player_code[player]:
                count_right_diag += 1
            
        if count_column == 3 or count_row == 3 or count_left_diag == 3 or count_right_diag == 3:
            return player
        else:
            return 0
        


# Your TicTacToe object will be instantiated and called as such:
toe = TicTacToe(3)
print(toe.move(0, 0, 1))
print(toe.move(0, 2, 2))
print(toe.move(2, 2, 1))
print(toe.move(1, 1, 2))
print(toe.move(2, 0, 1))
print(toe.move(1, 0, 2))
print(toe.move(2, 1, 1))