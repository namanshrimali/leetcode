class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.row_sums = [0] * n
        self.col_sums = [0] * n
        self.diagonal_sum = 0
        self.anti_diagonal_sum = 0
            
    def move(self, row: int, col: int, player: int) -> int:
        player_id = player
        player = 1 if player == 1 else -1
        self.row_sums[row] += player
        self.col_sums[col] += player
        if row == col:
            self.diagonal_sum += player
        if row == self.n - col - 1:
            self.anti_diagonal_sum += player
        
        mult_factor = player
        
        if self.row_sums[row] * mult_factor == self.n or self.col_sums[col] * mult_factor == self.n or self.anti_diagonal_sum * mult_factor == self.n or self.diagonal_sum * mult_factor == self.n:
            return player_id
        return 0
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)