class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = -1
        
        if nums[0] != 0: return 0
        for i in range(len(nums)):
            if nums[i] != i: 
                k = nums[i]
                break
        for i in range(len(nums)):
            if nums[i] != i: 
                k = k & nums[i]  

        return k if k!= -1 else 0
