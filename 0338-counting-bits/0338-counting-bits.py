class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0]*(n+1)
        for i in range(n+1):
            count = i
            while i:
                i = i & (i-1) # removes rightmost 1
                arr[count] += 1
        return arr