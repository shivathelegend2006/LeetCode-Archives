class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = 0
        if nums[0] != 0: return 0

        m = []
        for i in range(len(nums)):
            if nums[i] != i:
                m.append(nums[i])
        k = m[0] if m else 0
        for n in m:
            k = k&n
        return k
