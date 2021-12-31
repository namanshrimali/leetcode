class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [(-2, 1), (-2, -1),(2, 1), (2, -1), (-1, -2), (1, -2), (-1, 2), (1, 2)]
        visited = set()
        queue = collections.deque([(0, 0)])
        steps = 0
        while(queue):
            level_count = len(queue)
            for _ in range(level_count):
                curr_x, curr_y = queue.popleft()
                if (curr_x, curr_y) == (x, y):
                    return steps
                for x_dir, y_dir in directions:
                    next_x = curr_x+x_dir
                    next_y = curr_y+y_dir
                    
                    if (next_x, next_y) not in visited:
                        visited.add((next_x, next_y))
                        queue.append((next_x, next_y))
            steps+=1
                