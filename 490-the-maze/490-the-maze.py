class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set()
        m, n = len(maze), len(maze[0])
        queue = collections.deque([start])
        visited.add((start[0], start[1]))
        while queue:
            x, y = queue.popleft()
            
            if x == destination[0] and y == destination[1]:
                return True
            
            for x_dir, y_dir in directions:
                curr_x, curr_y = x, y
                while 0 <= curr_x+x_dir < m and 0 <= curr_y+y_dir < n and maze[curr_x+x_dir][curr_y+y_dir] == 0:
                    curr_x+=x_dir
                    curr_y+=y_dir
                if (curr_x, curr_y) not in visited:
                    queue.append([curr_x, curr_y])
                    visited.add((curr_x, curr_y))
        return False