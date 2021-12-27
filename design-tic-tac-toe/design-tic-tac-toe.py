class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.diagonal = 0
        self.anti_diagonal = 0
        self.rows = [0]*n
        self.cols = [0]*n
    
    def move(self, row: int, col: int, player: int) -> int:
        current_player = 1 if player == 1 else -1
        
        
        self.rows[row]+=current_player
        self.cols[col]+=current_player
        
        # checking diagonal
        if row == col:
            self.diagonal+=current_player
        
        # checking anti diagonal
        if (self.n-row-1)==col:
            self.anti_diagonal+=current_player
        
        # checking if row or col or diagonal or antidiagonal have value that hit n
        
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.diagonal) == self.n or abs(self.anti_diagonal)==self.n:
            return player
        
        return 0
        

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)