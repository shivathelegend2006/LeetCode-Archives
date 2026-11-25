class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        if len(nums) <= 1: return 0
        mods = [num % k for num in nums]
        min_cost = float('inf')
        
        for x in range(k):
            for y in range(k):
                if x == y: continue

                total = 0
                for i, val in enumerate(mods):
                    target = x if i %2 == 0 else y
                    diff = abs(val - target)
                    total += min(diff, k - diff)
                
                min_cost = min(total, min_cost)     
        return min_cost