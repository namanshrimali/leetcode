class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        m,  n = len(board), len(board[0])
        
        def find_word(row, col, suffix):
            if len(suffix) == 0:
                return True
            if not (-1 < row < m and -1 < col < n and board[row][col] == suffix[0]):
                return False
            is_found = False
            board[row][col] = '#'
            
            for x_dir, y_dir in directions:
                is_found = find_word(row+x_dir, col+y_dir, suffix[1:])
                
                if is_found:
                    break
            board[row][col] = suffix[0]
            return is_found
            
        for i in range(m):
            for j in range(n):
                if find_word(i, j, word):
                    return True
        return False