import heapq
from collections import defaultdict

class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)

        low, high = [], []
        sums = [0, 0]
        size = [0, 0]
        

        trash_low = defaultdict(int)
        trash_high = defaultdict(int)

        def clean(h, is_low):

            trash = trash_low if is_low else trash_high
            while h:
                val = -h[0] if is_low else h[0]
                if not trash[val]: break
                trash[val] -= 1
                heapq.heappop(h)

        def rebalance():
            if size[0] > size[1] + 1:
                clean(low, True)
                val = -heapq.heappop(low)
                sums[0] -= val; size[0] -= 1
                heapq.heappush(high, val)
                sums[1] += val; size[1] += 1

            elif size[1] > size[0]:
                clean(high, False)
                val = heapq.heappop(high)
                sums[1] -= val; size[1] -= 1
                heapq.heappush(low, -val)
                sums[0] += val; size[0] += 1

        costs = []
        for i, num in enumerate(nums):
            clean(low, True)
            if size[0] == 0 or num <= -low[0]:
                heapq.heappush(low, -num)
                sums[0] += num; size[0] += 1
            else:
                heapq.heappush(high, num)
                sums[1] += num; size[1] += 1

            if i >= x:
                out = nums[i - x]
                clean(low, True)

                if size[0] > 0 and out <= -low[0]:
                    sums[0] -= out; size[0] -= 1
                    trash_low[out] += 1
                else:
                    sums[1] -= out; size[1] -= 1
                    trash_high[out] += 1

            rebalance()
            if i >= x - 1:
                clean(low, True)
                cost = sums[1] - sums[0] + (-low[0] if size[0] > size[1] else 0)
                costs.append(cost)

        m = len(costs)

        dp = [0] * (m + 1)
        for j in range(1, k + 1):
            curr = [float('inf')] * (m + 1)
            for i in range(1, m + 1):
                skip = curr[i - 1]
                take = dp[max(0, i - x)] + costs[i - 1]
                curr[i] = min(skip, take) 

            dp = curr

        return dp[m]