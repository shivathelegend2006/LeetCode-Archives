class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #basically a binary tree, so do dfs on it till u reach the target
        table = {}
        def dfs(i, curr):
            if (i,curr) in table:
                return table[(i,curr)]
            if i == len(nums):
                return 1 if curr == target else 0
            
            add = dfs(i+1, curr + nums[i])
            sub = dfs(i+1, curr - nums[i])

            table[(i,curr)] = add + sub
            return table[(i,curr)]

        return dfs(0,0)