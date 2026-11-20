class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        hs = set()

        arr1 = [str(x) for x in arr1]
        arr2 = [str(x) for x in arr2]

        for x in arr1:
            for i in range(1, len(x) + 1):
                hs.add(x[:i])

        length = 0
        for x in arr2:
            for i in range(1, len(x) + 1):
                if x[:i] in hs:
                    length = max(length, len(x[:i]))

        return length