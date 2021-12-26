class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)-1
        if grid[0][0]!=0 or grid[n][n]!=0:
            return -1
        
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        def get_neighbours(row, col):
            for row_diff, col_diff in directions:
                new_row = row+row_diff
                new_col = col+col_diff
                if not(0<=new_row<=n and 0<=new_col<=n):
                    continue
                if grid[new_row][new_col]!=0:
                    continue
                yield((new_row, new_col))
        
        queue=collections.deque([(0,0, 1)])
        visited = set()
        visited.add((0,0))
        
        while(queue):
            row, col, distance = queue.popleft()
            if grid[row][col]!=0:
                continue
            if (row, col) == (n, n):
                return distance
            for neighbour in get_neighbours(row, col):
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((*neighbour, distance+1))
        return -1
            