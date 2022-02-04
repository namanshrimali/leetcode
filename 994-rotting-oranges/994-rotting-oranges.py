class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        m, n = len(grid), len(grid[0])
        
            
        rotten = collections.deque([])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2: # rotten orange found
                    rotten.append([row, col])
        time = 0
        while rotten:
            rot_len = len(rotten)
            for _ in range(rot_len):
                row, col = rotten.popleft()
                
                for row_dir, col_dir in directions:
                    row_dir, col_dir = row+row_dir, col+col_dir
                    if -1 < row_dir < m and -1 < col_dir < n and grid[row_dir][col_dir] == 1:
                        grid[row_dir][col_dir] = 2
                        rotten.append([row_dir, col_dir])
            if rotten:
                time+=1

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1: # fresh orange found
                    return -1
        return time