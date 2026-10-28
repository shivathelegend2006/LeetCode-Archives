class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid) #row
        n = len(grid[0]) #col

        dp = [set() for i in range(n)]

        dp[0].add(grid[0][0])

        for i in range(1,n):
            dp[i] = { xor ^ grid[0][i] for xor in dp[i-1]}

        for r in range(1,m):
            dp[0] = {xor ^ grid[r][0] for xor in dp[0]}

            for c in range(1,n):
                dp[c] = {xor ^ grid[r][c] for xor in (dp[c] | dp[c-1])}

        return min(dp[-1]) 