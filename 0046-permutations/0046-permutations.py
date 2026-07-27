class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        #there are two ways,
        #1. imagine that the list ia a complete grpahw ith all nodes connected to wach other and now perform dfs recrusivly till u find it
        # OR, perform pklaxce swapping, lock in a varib ale and continuously swap the ret for all combinations

        def bt(start):
            if start == len(nums):
                res.append(list(nums))

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                bt(start +1)
                nums[start], nums[i] = nums[i], nums[start] #reverse the swap
        bt(0)
        return res