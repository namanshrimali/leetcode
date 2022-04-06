class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])
        
        def bfs(i, j):
            deque = collections.deque([(i, j)])
            grid[i][j] = "0"
            while deque:
                curr_x, curr_y = deque.popleft()
                for x, y in directions:
                    next_x, next_y = curr_x+x, curr_y+y
                    if -1<next_x<m and -1<next_y<n and grid[next_x][next_y] != "X" and not grid[next_x][next_y].isdigit():
                        next_dist = str(int(grid[curr_x][curr_y])+1)
                        if grid[next_x][next_y] == '#':
                            return int(next_dist)
                        grid[next_x][next_y] = next_dist
                        deque.append((next_x, next_y))
                        
            return -1
                        
        min_distance = inf
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    distance = bfs(i, j)
                    if distance != -1:
                        min_distance = min(min_distance, distance)
        
        return -1 if min_distance==inf else min_distance