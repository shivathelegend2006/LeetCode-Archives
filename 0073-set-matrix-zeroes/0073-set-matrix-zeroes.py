class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        

        col0_is_zero = False

        for r in range(ROWS):

            if matrix[r][0] == 0:
                col0_is_zero = True
                

            for c in range(1, COLS):
                if matrix[r][c] == 0:
      
                    matrix[0][c] = 0
                    matrix[r][0] = 0
                    

        for r in range(1, ROWS):
            for c in range(1, COLS):

                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
                    

        if matrix[0][0] == 0:
            for c in range(COLS):
                matrix[0][c] = 0

        if col0_is_zero:
            for r in range(ROWS):
                matrix[r][0] = 0