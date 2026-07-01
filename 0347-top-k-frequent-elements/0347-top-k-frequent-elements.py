class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for i in nums:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1

        hash = sorted(hash.items(),key=lambda x : x[1], reverse = True)
        result = []
        for i in range(k):
            result.append(hash[i][0])

        return result