class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            nonlocal count
            if not (-1<row<len(grid)) or not (-1<col<len(grid[0])) or grid[row][col] == 0:
                return
            count+=1
            grid[row][col] = 0
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
        
        max_island = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    count = 0
                    dfs(i, j)
                    max_island = max(max_island, count)
        
        return max_island
            