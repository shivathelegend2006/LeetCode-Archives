class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #do dfs from any edge 0 thn chbg eit to T or S, hen normaly sweep accros and invert any interior 0 to x and ts to 0 and return 

        row, col = len(board), len(board[0])

        def dfs(r,c):
            if (r <0 or c < 0 or r== row or c == col or board[r][c] != "O"): return


            board[r][c] = "T"

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r, c+1)
            dfs(r, c-1)


        for r in range(row):
            for c in  range(col):
                if r == 0 or r == row -1 or c == 0 or c == col-1:
                    if board[r][c] == "O": dfs(r,c)

        for r in range(row):
            for c in  range(col):
                if board[r][c] == "O": board[r][c] = "X"
                elif board[r][c] == "T": board[r][c] = "O"


           