class TicTacToe:

    def __init__(self, n: int):
        self.row_sum = [0] * n
        self.col_sum = [0] * n
        self.diag_sum = 0
        self.anti_diag_sum = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        player_offset = 1 if player == 1 else -1
        n = self.n
        self.row_sum[row] += player_offset
        self.col_sum[col] += player_offset
        if row == col:
            self.diag_sum += player_offset
        if row == n - col - 1:
            self.anti_diag_sum += player_offset
        
        if self.row_sum[row] in (n, -n) or self.col_sum[col] in (n, -n) or self.diag_sum in (n, -n) or self.anti_diag_sum in (n, -n):
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)