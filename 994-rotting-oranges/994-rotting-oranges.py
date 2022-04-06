class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        total_fresh_oranges = 0
        rotten = collections.deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total_fresh_oranges +=1
                if grid[i][j] == 2:
                    rotten.append((i, j))
        if total_fresh_oranges == 0:
            return 0
        timer = -1
        while rotten:
            deque_len = len(rotten)
            for _ in range(deque_len):
                i, j = rotten.popleft()
                for x, y in directions:
                    if -1<i+x<m and -1<j+y<n and grid[i+x][j+y] == 1:
                        grid[i+x][j+y] = 2
                        total_fresh_oranges -=1
                        rotten.append((i+x, j+y))
            timer+=1
        
        return -1 if total_fresh_oranges > 0 else timer
        