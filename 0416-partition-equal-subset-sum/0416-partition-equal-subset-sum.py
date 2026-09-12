class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        sums = {0}
        for n in nums:
            new = {curr + n for curr in sums}
            sums.update(new)

        return True if sum(nums)/2 in sums else False
