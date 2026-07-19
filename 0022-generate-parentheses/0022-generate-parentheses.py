class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #we use bakctrajcing
        res = []

        def bt(open,close,curr):
            if open == close == n:
                res.append(curr)
                return

            if open < n:
                bt(open+1,close,curr+"(")

            if close < open:
                bt(open,close+1,curr+")")

        bt(0,0,"")
        return res