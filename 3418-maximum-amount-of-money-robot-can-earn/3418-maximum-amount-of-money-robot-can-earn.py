class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m,n = len(coins), len(coins[0])
        ni = float('-inf')

        dp = [[[ni]*3 for i in range(n)]for j in range(m)]

        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    continue

                val = coins[i][j]

                for k in range(3):
                    bp = ni
                    if i > 0:
                        bp = max(bp, dp[i-1][j][k])
                    if j > 0:
                        bp = max(bp, dp[i][j-1][k])

                    if bp != ni:
                        dp[i][j][k] = max(dp[i][j][k], bp + val)

                    if val < 0 and k > 0:
                        pk = ni
                        if i > 0 :
                            pk = max(pk, dp[i-1][j][k-1])
                        if j > 0:
                            pk = max(pk, dp[i][j-1][k-1])
                        if pk != ni:
                            dp[i][j][k] = max(dp[i][j][k], pk)

        return max(dp[m-1][n-1]) 