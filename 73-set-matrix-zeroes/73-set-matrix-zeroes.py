class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        is_first_col_nulled = False
        for i in range(m):
            if matrix[i][0] == 0:
                is_first_col_nulled = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if not (matrix[i][0] and matrix[0][j]):
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for i in range(n):
                matrix[0][i] = 0
        
        if is_first_col_nulled:
            for i in range(m):
                matrix[i][0] = 0