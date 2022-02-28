class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(matrix), len(matrix[0])
        remaining = m*n - 1
        curr_x, curr_y = 0, 0
        answer = [matrix[0][0]]
        matrix[0][0] = -inf

        while remaining:
            for next_x, next_y in directions:
                while -1 < curr_x + next_x < m and -1 < curr_y + next_y < n and matrix[curr_x+next_x][curr_y + next_y] != -inf:
                    curr_x += next_x
                    curr_y += next_y
                    answer.append(matrix[curr_x][curr_y])
                    matrix[curr_x][curr_y] = -inf
                    remaining-=1
                    
        return answer
        