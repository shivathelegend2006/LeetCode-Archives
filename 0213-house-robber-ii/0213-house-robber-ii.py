class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]

        def best_rob(nums):
            max1,max2 = 0,0

            for i in nums:
                curr = max(max1 + i,max2) #rob current house and keep two houses back loot or skip current house
                max1 = max2
                max2 = curr

            return max2

        return max(best_rob(nums[1:]),best_rob(nums[:-1]))