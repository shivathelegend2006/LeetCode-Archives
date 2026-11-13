class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        without_rearrangment = sum(abs(a-b) for a, b in zip(arr,brr))

        arr.sort()
        brr.sort()
        with_rearrangement = k + sum(abs(a-b) for a, b in zip(arr,brr))

        return min(without_rearrangment,with_rearrangement )