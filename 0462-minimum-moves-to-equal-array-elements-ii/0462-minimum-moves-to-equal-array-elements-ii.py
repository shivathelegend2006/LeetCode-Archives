class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        s = sorted(nums)
        anchor = s[len(s)//2]
        count = 0
        for n in nums:
            count += abs(n - anchor)

        return count