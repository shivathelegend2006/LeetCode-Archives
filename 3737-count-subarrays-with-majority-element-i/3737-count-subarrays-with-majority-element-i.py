
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(len(nums)):
            target_count = 0
            for j in range(i,len(nums)):
                if nums[j] == target:
                    target_count += 1
                if target_count > (j-i+1)//2:
                    count += 1
        return count