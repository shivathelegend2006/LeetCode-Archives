class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        if k == 0: return s
        sl = list(s)

        for i in range(len(sl)):
            if k == 0:
                break

            ch = sl[i]
            dist = min(ord(ch) - ord('a'), 26 - (ord(ch) - ord('a')))

            if k >= dist:
                sl[i] = 'a'
                k -= dist
            
            else:
                sl[i] = chr(ord(ch) - k)
                k = 0

        return "".join(sl)