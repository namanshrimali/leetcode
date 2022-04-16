class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        direction_letter = ['U', 'D', 'R', 'L']
        m, n = len(grid), len(grid[0])
        
        def dfs(x, y):
            nonlocal curr_pattern
            grid[x][y] = 0
            
            for i, (x_dir, y_dir) in enumerate(directions):
                new_x, new_y = x+x_dir, y+y_dir
                if -1 < new_x < m and -1 < new_y < n and grid[new_x][new_y] == 1:
                    curr_pattern.append(direction_letter[i])
                    dfs(new_x, new_y)
                    curr_pattern.append('0')
        
        seen = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    curr_pattern = ['S']
                    
                    dfs(i, j)
                    seen.add(''.join(curr_pattern))
        
        return len(seen)
        