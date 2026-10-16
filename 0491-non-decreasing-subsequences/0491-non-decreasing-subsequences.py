class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        ans = []
        def bt(idx,chain):
            if len(chain) >= 2:
                ans.append(chain[:])

            level = set()
            for i in range(idx,len(nums)):
                if nums[i] in level:
                    continue
                
                if chain and nums[i] < chain[-1]:
                    continue

                level.add(nums[i])
                chain.append(nums[i])
                bt(i + 1, chain)
                chain.pop()

        bt(0,[])
        return ans
