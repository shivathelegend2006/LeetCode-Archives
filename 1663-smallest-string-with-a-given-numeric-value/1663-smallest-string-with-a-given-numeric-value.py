class Solution:
    def getSmallestString(self, n: int, k: int) -> str:

        k -= n
        zs = k //25
        r = k % 25

        mid = chr(ord("a") + r) if r > 0 else ""

        a_s = n - zs - (1 if r > 0 else 0)

        return ("a"*a_s) + mid + ("z"*zs)

