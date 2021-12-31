class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        EMPTY = 2147483647
        queue = collections.deque()
        max_rows = len(rooms)
        max_cols = len(rooms[0])
        for row in range(max_rows):
            for col in range(max_cols):
                if rooms[row][col] == 0:
                    queue.append((row, col))
        
        while(queue):
            row, col = queue.popleft()
            for row_dir, col_dir in directions:
                next_row, next_col = row+row_dir, col+col_dir
                if not (-1<next_row<max_rows) or not (-1<next_col<max_cols) or rooms[next_row][next_col] != EMPTY:
                    continue
                rooms[next_row][next_col] = rooms[row][col] + 1
                queue.append((next_row, next_col))
        
                
            