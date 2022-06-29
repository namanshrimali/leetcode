class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        total_players = 2
        are_moves_possible = len(moves) < n**2
        curr_player = 0
        move_sum_per_row = [0] * n
        move_sum_per_col = [0] * n
        anti_diag_sum = 0
        diag_sum = 0
        has_won = False
        
        def is_diagonal(row, col):
            return row == col
        def is_anti_diagonal(row, col):
            return row == n - col - 1
        def has_row_crossed(row):
            return move_sum_per_row[row] in (n, -n)
        def has_column_crossed(col):
            return move_sum_per_col[col] in (n, -n)
        
        def has_diag_crossed_for_player(player):
            if player == 0:
                return diag_sum == n
            return diag_sum == -n
        
        def has_anti_diag_crossed_for_player(player):
            if player == 0:
                return anti_diag_sum == n
            return anti_diag_sum == -n
        
        def get_move(player):
            return 1 if player == 0 else -1
        
        for row, col in moves:
            move = get_move(curr_player)
            move_sum_per_row[row] += move
            move_sum_per_col[col] += move
            
            if is_diagonal(row, col):
                diag_sum+=move
            
            if is_anti_diagonal(row, col):
                anti_diag_sum += move
            
            if has_row_crossed(row) or has_column_crossed(col) or has_diag_crossed_for_player(curr_player) or has_anti_diag_crossed_for_player(curr_player):
                has_won = True
                break
            
            curr_player = (curr_player + 1)%total_players
        
        if has_won:
            return "A" if curr_player == 0 else "B"
        elif are_moves_possible:
            return "Pending"
        else:
            return "Draw"
        