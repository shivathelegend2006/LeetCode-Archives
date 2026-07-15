class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')

        for i in range(len(nums) - 2):
            left = i+1
            right = len(nums) - 1

            while left < right:
                curr = nums[i] + nums[left] + nums[right]

                if abs(target - curr) < abs(target - closest):
                    closest = curr

                if curr < target:
                    left += 1
                elif curr > target:
                    right -= 1

                else:
                    return curr

        return closest