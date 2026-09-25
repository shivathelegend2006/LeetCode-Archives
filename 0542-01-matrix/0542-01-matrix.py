class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] > 0:
                    top = mat[r-1][c] if r > 0 else float('inf')
                    left = mat[r][c-1] if c > 0 else float('inf')
                    mat[r][c] = min(top,left) + 1

        for r in range(len(mat) - 1, -1 , -1):
            for c in range(len(mat[0]) -1 , -1 , -1):
                if mat[r][c] > 0:
                    down = mat[r+1][c] if r < len(mat)-1 else float('inf')
                    right = mat[r][c+1] if c < len(mat[0]) - 1 else float('inf')
                    mat[r][c] = min(mat[r][c], down + 1, right + 1)


        return mat