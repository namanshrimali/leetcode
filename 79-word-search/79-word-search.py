class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        def coordinates_are_valid(x, y):
            return -1 < x < m and -1 < y < n
        
        def find_word(x, y, suffix):
            if len(suffix)  == 0:
                return True
            if not coordinates_are_valid(x, y) or board[x][y] != suffix[0]:
                return False

            board[x][y] = '#'
            for x_dir, y_dir in directions:
                is_found = find_word(x+x_dir, y+y_dir, suffix[1:])
                if is_found:
                    break
            board[x][y] = suffix[0]
            return is_found
                
            
        for i in range(m):
            for j in range(n):
                if find_word(i, j, word):
                    return True
        return False