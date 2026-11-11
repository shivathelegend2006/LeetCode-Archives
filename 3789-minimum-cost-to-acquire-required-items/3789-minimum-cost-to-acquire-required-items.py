class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        c1, c2, cb = cost1, cost2, costBoth

        cost = 0
        cost += min(cb, c1+c2)*min(need1,need2)
        if need1 < need2:
            need2 -= need1
            need1 = 0
        else:
            need1 -= need2
            need2 = 0
        
        cost += min(cb, c1)*need1
        cost += min(cb,c2)*need2

        return cost

        