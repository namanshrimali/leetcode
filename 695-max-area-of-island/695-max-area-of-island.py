class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        
        def dfs(x, y):
            nonlocal area
            
            area += 1
            grid[x][y] = 0
            
            for x_dir, y_dir in directions:
                new_x, new_y = x+x_dir, y+y_dir
                
                if -1 < new_x < m and -1 < new_y < n and grid[new_x][new_y] == 1:
                    dfs(new_x, new_y)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i, j)
                    max_area = max(area, max_area)
        return max_area
        