class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        
        def bfs(deque, fresh_oranges):
            counter = -1
            while deque:
                que_len = len(deque)
                for _ in range(que_len):
                    curr_x, curr_y = deque.popleft()
                    for x, y in directions:
                        new_x, new_y = curr_x+x, curr_y+y
                        if -1 < new_x < m and -1 < new_y < n and grid[new_x][new_y] == 1:
                            grid[new_x][new_y] = 2
                            fresh_oranges -= 1
                            deque.append((new_x, new_y))
                counter+=1
            return counter if fresh_oranges == 0 else -1
        
        fresh_oranges, deque = 0, collections.deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_oranges+=1
                if grid[i][j] == 2:
                    deque.append((i, j))
        return bfs(deque, fresh_oranges) if fresh_oranges else 0
                
        