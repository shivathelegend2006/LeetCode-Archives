class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        mod = 10**9 + 7

        even, odd = 1,0
        curr, res = 0,0

        for num in arr:
            curr += num
            if curr % 2 == 1:
                res += even
                odd += 1
            else:
                res += odd
                even += 1
            res %= mod

        return res 