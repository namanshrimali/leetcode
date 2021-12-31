class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(row, col):
            nonlocal diameter
            if (row, col) in visited:
                return
            if not(-1<row<len(grid)) or not(-1<col<len(grid[0])) or grid[row][col] != 1:
                diameter+=1
                return
            visited.add((row, col))
            for x_dir, y_dir in directions:
                dfs(row+x_dir, col+y_dir)
                
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        diameter = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in visited and grid[i][j] == 1:
                    dfs(i, j)
        return diameter
    