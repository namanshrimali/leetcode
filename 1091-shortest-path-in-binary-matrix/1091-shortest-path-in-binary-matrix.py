class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        if grid[0][0] != 0 or grid[m-1][n-1] != 0:
            return -1
        
        def are_coordinates_valid(x, y):
            return -1 < x < m and -1 < y < n and grid[x][y] != 1
        
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        curr_path_len = 0
        deque = collections.deque([(0, 0)])
        grid[0][0] = 1
        while deque:
            curr_path_len += 1
            deque_len = len(deque)
            for _ in range(deque_len):
                curr_x, curr_y = deque.popleft()
                if (curr_x, curr_y) == (m-1, n-1):
                    return curr_path_len
                for x_dir, y_dir in directions:
                    next_x, next_y = curr_x + x_dir, curr_y + y_dir
                    if are_coordinates_valid(next_x, next_y):
                        grid[next_x][next_y] = 1
                        deque.append((next_x, next_y))
        return -1
