class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = triangle[-1][:]
        t = triangle
        for r in range(len(t) -2 , -1, -1):
            for c in range(len(t[r])):
                dp[c] = t[r][c] + min(dp[c], dp[c+1])

        return dp[0]