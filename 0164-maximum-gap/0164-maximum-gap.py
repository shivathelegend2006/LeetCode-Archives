class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) < 2: return 0
        nums.sort()
        maxDiff = nums[1]- nums[0]
        diff = maxDiff
        for i in range(1,len(nums)):
            diff = nums[i] - nums[i-1]
            maxDiff = max(maxDiff, diff)

        return maxDiff