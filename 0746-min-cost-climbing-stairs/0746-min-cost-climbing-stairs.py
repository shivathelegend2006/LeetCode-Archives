class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1],cost[i-2])
        n = len(cost)
        return min(cost[n-1],cost[n-2])
