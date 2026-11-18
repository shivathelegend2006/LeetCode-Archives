class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [-1]*(target + 1)
        dp[0] = 0

        for n in nums:
            for t in range(target, n - 1, -1):
                if dp[t-n] != -1:
                    dp[t] = max(dp[t], dp[t-n] + 1)

        return dp[target]