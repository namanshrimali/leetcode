class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def bfs(row, col):
            food_found = False
            deque = collections.deque([(row, col)])
            path_len = 0
            while deque and not food_found:
                deque_len = len(deque)
                for _ in range(deque_len):
                    curr_row, curr_col = deque.popleft()
                    for x, y in directions:
                        next_row, next_col = curr_row+x, curr_col+y
                        
                        if not (-1 < next_row < m and -1 < next_col < n):
                            continue
                        elif grid[next_row][next_col] == 'X':
                            continue  
                        elif grid[next_row][next_col] == '#':
                            food_found = True
                            break
                        else:
                            grid[next_row][next_col] = 'X'
                        deque.append((next_row, next_col))
                path_len +=1
            return path_len if food_found else -1
        
        for row in range(m):
            for col in range(n):
                if grid[row][col]=='*':
                    grid[row][col] = 'X'
                    return bfs(row, col)
        