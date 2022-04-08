class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        
        def bfs(start_x, start_y):
            grid[start_x][start_y] = 0
            deque = collections.deque([(start_x, start_y)])
            
            while deque:
                que_len = len(deque)
                for _ in range(que_len):
                    curr_x, curr_y = deque.popleft()
                    for x, y in directions:
                        new_x, new_y = curr_x + x, curr_y + y
                        if -1 < new_x < m and -1 < new_y < n:
                            if grid[new_x][new_y] == '#':
                                return grid[curr_x][curr_y]+1
                            if grid[new_x][new_y] == 'O':
                                grid[new_x][new_y] = grid[curr_x][curr_y]+1
                                deque.append((new_x, new_y))
            return -1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    return bfs(i, j)