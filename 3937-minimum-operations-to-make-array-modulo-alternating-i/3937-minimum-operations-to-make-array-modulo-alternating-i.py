class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        if len(nums) <= 1: return 0
        evens = [nums[i] % k for i in range(0, len(nums), 2)]
        odds = [nums[i] % k for i in range(1, len(nums), 2)]

        def top2(arr):
            best = [(float('inf'), - 1), (float('inf'), - 1)]
            for target in range(k):
                total = 0
                for x in arr:
                    diff = abs(x - target)
                    total += min(diff, k - diff)

                if total < best[0][0]: #if its lower than best cost
                    best[1] = best[0]
                    best[0] = (total, target)
                elif total < best[1][0]:
                    best[1] = (total, target)

            return best

        e1, e2 = top2(evens)
        o1, o2 = top2(odds)

        if e1[1] != o1[1]:
            return e1[0] + o1[0]

        return min(e1[0] + o2[0], e2[0] + o1[0])