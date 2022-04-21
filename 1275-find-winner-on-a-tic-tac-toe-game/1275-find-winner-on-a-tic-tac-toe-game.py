class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        might_be_pending = len(moves) < 9
        curr_player = 1 # A is 1, B is -1
        winner = None
        row_total = [0]*3
        col_total = [0]*3
        diag_total = 0
        anti_diag_total = 0
        
        for row, col in moves:
            col_total[col] += curr_player
            row_total[row] += curr_player
            if row == col:
                diag_total += curr_player
            if row == 3-col-1:
                anti_diag_total += curr_player
            
            if row_total[row] in (-3, 3) or col_total[col] in (-3, 3) or diag_total in (-3, 3) or anti_diag_total in (-3, 3):
                winner = curr_player
                break
                
            curr_player = - curr_player
        
        if winner:
            return 'A' if winner == 1 else 'B'
        elif might_be_pending:
            return 'Pending'
        else:
            return 'Draw'
            