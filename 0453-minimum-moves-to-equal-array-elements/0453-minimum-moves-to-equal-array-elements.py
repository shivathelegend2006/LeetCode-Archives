class Solution:
    def minMoves(self, nums: list[int]) -> int:
        m = min(nums)
        count = 0
        for n in nums:
            count += n - m

        return count