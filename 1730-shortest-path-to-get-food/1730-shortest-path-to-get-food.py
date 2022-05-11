class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        curr_distance = -1
        deque = collections.deque([])
        m, n = len(grid), len(grid[0])
        
        # iterating over grid to find starting point and placing it on deque
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    deque.append((i, j))
                    grid[i][j] = 'X'    # marking it as obstacle so that it won't be selected again in future
                    break
        
        # finding food
        while deque:
            curr_distance += 1
            for _ in range(len(deque)):
                curr_x, curr_y = deque.popleft()
                for x, y in directions:
                    next_x, next_y = curr_x + x, curr_y + y
                    if -1 < next_x < m and -1 < next_y < n and grid[next_x][next_y] in '#O':
                        if grid[next_x][next_y] == '#':  # food found
                            return curr_distance + 1
                        deque.append((next_x, next_y))
                        grid[next_x][next_y] = 'X'
                
        return -1