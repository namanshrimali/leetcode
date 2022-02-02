class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        diagonal, anti_diagonal = 0, 0
        row, col = [0, 0, 0], [0, 0, 0]
        
        move = 1
        for move_x, move_y in moves:
            if move%2==1:
                update = 1
            else:
                update = -1
            row[move_x]+=update
            col[move_y]+=update
            if (move_x, move_y) in [(0, 0), (1,1), (2,2)]:
                diagonal+=update
            if (move_x, move_y) in [(0,2), (1,1), (2, 0)]:
                anti_diagonal+=update
            move+=1
        if diagonal == 3 or anti_diagonal == 3 or 3 in row or 3 in col:
            return "A"
        elif diagonal == -3 or anti_diagonal == -3 or -3 in row or -3 in col:
            return "B"
        elif move<=9:
            return "Pending"
        else:
            return "Draw"