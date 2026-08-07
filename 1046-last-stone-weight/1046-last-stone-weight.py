class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # 8, 7, 4, 2, 1, 1
        while len(stones) > 1:
            stones.sort(reverse = True)

            s1 = stones[0]
            s2 = stones[1]
            stones.pop(0)
            stones.pop(0)

            if s1 != s2:
                stones.append(s1 - s2)
        return stones[0] if stones else 0