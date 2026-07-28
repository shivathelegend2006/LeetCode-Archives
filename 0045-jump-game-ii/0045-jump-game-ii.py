class Solution:
    def jump(self, nums: List[int]) -> int:
        #greeeeeeedy
        jumps= 0
        end = 0
        furthest = 0

        for i in range(len(nums)-1):
            furthest = max(furthest , i+nums[i])
            if i == end:
                jumps += 1
                end = furthest
                if end >= len(nums)-1:
                    break
        return jumps