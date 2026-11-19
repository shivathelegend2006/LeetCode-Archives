import heapq
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        s = heapq.nsmallest(3,nums)
        l = heapq.nlargest(3, nums)
        return min(l[0] - s[2], l[1] - s[1], l[2] - s[0])

        