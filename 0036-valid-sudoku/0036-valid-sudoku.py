from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set) #default dict is a special tool from collections lrivbary to skip initialisation conditions 

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                val = board[r][c]
                if (val in rows[r]) or (val in col[c]) or (val in box[(r//3,c//3)]):
                    return False

                rows[r].add(val)
                col[c].add(val)
                box[(r//3,c//3)].add(val)

        return True