class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        hold = float('-inf')
        sold = 0
        rest = 0

        for p in prices:
            prev = sold
            sold = hold + p
            hold = max(hold, rest - p)
            rest = max(prev, rest)

        return max(sold, rest) 