class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        s = ["a"]*n
        k -= n
        for i in range(n-1,-1,-1):
            if k == 0: break

            if k >= 25:
                s[i] = "z"
                k -= 25
            
            else:
                s[i] = chr(ord("a") + k)
                k = 0

        return "".join(s)

