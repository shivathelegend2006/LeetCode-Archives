class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        score = len(nums)*[1]

        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    score[i] = max(score[i],score[j]+1)

        return max(score)