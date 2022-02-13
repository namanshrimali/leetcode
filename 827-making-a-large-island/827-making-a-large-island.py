class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        island_id = -1
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        island_size_dict = {}
        m, n = len(grid), len(grid[0])
        
        def dfs(row, col):
            grid[row][col] = island_id
            
            island_size_dict[island_id] = island_size_dict.get(island_id, 0)+1
            
            for row_dir, col_dir in directions:
                next_row, next_col = row+row_dir, col+col_dir
                if 0 <= next_row < m and 0 <= next_col < n and grid[next_row][next_col] == 1:
                    dfs(next_row, next_col)
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    dfs(row, col)
                    island_id-=1
        if island_size_dict:
            max_size = max(island_size_dict.values())
            for row in range(m):
                for col in range(n):
                    if grid[row][col] == 0:
                        islands = set()
                        # get islands from all directions
                        for row_dir, col_dir in directions:
                            next_row, next_col = row+row_dir, col+col_dir
                            if 0<=next_row<m and 0<=next_col<n and grid[next_row][next_col] != 0:
                                islands.add(grid[next_row][next_col])
                        new_size = 1
                        for island in islands:
                            new_size+=island_size_dict[island]
                        max_size = max(max_size, new_size)
            return max_size
        return 1
                    