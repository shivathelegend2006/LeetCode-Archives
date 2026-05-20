class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for n in range(len(nums)):
            if nums[x] > nums[n]:
                x = n

        return nums[x]