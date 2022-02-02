class Solution:
    
    def has_won(self, tictac):
        # diagonal check
        if tictac[1][1]!=0 and (tictac[0][0] == tictac[1][1] == tictac[2][2] or tictac[0][2] ==  tictac[1][1] == tictac[2][0]):
            return True
        
        for i in range(3):
            if tictac[i][0]!=0 and tictac[i][0] == tictac[i][1] == tictac[i][2] or tictac[0][i]!=0 and tictac[0][i] == tictac[1][i]== tictac[2][i]:
                return True
        return False
    
    def tictactoe(self, moves: List[List[int]]) -> str:
        tictac = [[0 for _ in range(3)] for _ in range(3)]
        
        total_moves = 9-len(moves)
        a_won, b_won = False, False
        
        for i in range(len(moves)):
            tictac[moves[i][0]][moves[i][1]] = 'X' if i%2==0 else 'O'
            if self.has_won(tictac):
                if i%2==0:
                    a_won = True
                else:
                    b_won = True
                break
        if a_won:
            return "A"
        elif b_won:
            return "B"
        elif total_moves !=0:
            return "Pending"
        else:
            return "Draw"