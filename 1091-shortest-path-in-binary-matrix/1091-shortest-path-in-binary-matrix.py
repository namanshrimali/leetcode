class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        deque = collections.deque([(0, 0)])
        grid[0][0] = -1

        while deque:
            curr_x, curr_y = deque.popleft()
            
            if grid[curr_x][curr_y] == '*':
                continue
            
            curr_path = -grid[curr_x][curr_y]
            
            if (curr_x, curr_y) == (n-1, n-1):
                return curr_path

            for x, y in directions:
                next_x, next_y = curr_x + x, curr_y + y
                if -1 < next_x < n and -1 < next_y < n and grid[next_x][next_y] == 0:
                    deque.append((next_x, next_y))
                    grid[next_x][next_y] = - curr_path - 1

            grid[curr_x][curr_y] = '*'
            
        return -1
        