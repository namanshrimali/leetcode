class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        
        def find_connected(row, col):
            queue = collections.deque([(row, col)])
            while queue:
                curr_row, curr_col = queue.popleft()
                for x, y in directions:
                    next_row, next_col = curr_row+x, curr_col+y
                    if -1 < next_row < m and -1 < next_col < n and grid[next_row][next_col] == '1':
                        grid[next_row][next_col] = '0'
                        queue.append((next_row, next_col))
            
                    
        num_of_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    num_of_islands +=1
                    find_connected(i, j)
        return num_of_islands