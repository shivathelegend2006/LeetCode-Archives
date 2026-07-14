class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows= [""]  * numRows

        curr = 0
        step = 1

        for char in s:
            rows[curr] += char

            if curr == 0:
                step = 1
            elif curr == numRows - 1:
                step = -1

            curr += step

        return "".join(rows)