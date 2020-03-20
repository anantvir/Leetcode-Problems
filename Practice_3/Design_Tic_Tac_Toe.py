class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rowCounter = [0]*n
        self.colCounter = [0]*n
        self.leftDiag = 0
        self.rightDiag = 0
        self.n = n

    def move(self, row, col, player):
        """
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        move = 1 if player == 1 else -1
        self.rowCounter[row] += move
        self.colCounter[col] += move
        if row == col:
            self.leftDiag += move
        if row == self.n - col - 1:     # If r = n-c-1
            self.rightDiag += move
        if self.rowCounter[row] == self.n or self.colCounter[col] == self.n or self.leftDiag == self.n or self.rightDiag == self.n:
            return 1
        elif self.rowCounter[row] == -self.n or self.colCounter[col] == -self.n or self.leftDiag == -self.n or self.rightDiag == -self.n:
            return 2
        else:
            return 0



        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)