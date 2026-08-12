class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #classic 2d dp
        if len(s1)+ len(s2) != len(s3): return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True

        #filling 1st col
        for i in range(1,len(s1)+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1] #if ot matches and the left is true

        #filling top row
        for j in range(1,len(s2)+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        #filling table
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):

                if_s1 = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                if_s2 = dp[i][j-1] and s2[j-1] == s3[i+j-1]

                dp[i][j] = if_s1 or if_s2

        return dp[len(s1)][len(s2)]