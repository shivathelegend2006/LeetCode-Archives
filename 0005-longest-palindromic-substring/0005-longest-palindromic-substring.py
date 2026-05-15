class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[False]*n for i in range(n)]
        pal = ""
        max = 0

        for i in range(n-1,-1,-1):
            for j in range (i,n):
                if s[i]==s[j] and (j-i <= 1 or dp[i+1][j-1]==True):
                    dp[i][j] = True
                    curr = j-i+1
                    if curr > max:
                        max = curr
                        pal = s[i:j+1]
        return pal
        