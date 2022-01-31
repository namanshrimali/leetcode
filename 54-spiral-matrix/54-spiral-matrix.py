class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        sol = []
        m, n = len(matrix), len(matrix[0])
        total_elements, boundry = m*n, 0
        direction, i, j = 'R', 0, 0
        while total_elements:
            sol.append(matrix[i][j])
            if direction == 'R':
                if j+1 < n-boundry:
                    j+=1
                else:
                    direction = 'D'
                    i+=1
            elif direction == 'L':
                if j-1 >= boundry:
                    j-=1
                else:
                    direction = 'U'
                    i-=1
            elif direction == 'D':
                if i+1 < m-boundry:
                    i+=1
                else:
                    direction = 'L'
                    j-=1
            else: # direction == 'U'
                if i-1 > boundry:
                    i-=1
                else:
                    direction = 'R'
                    j+=1
                    boundry+=1
            total_elements-=1
        return sol
        