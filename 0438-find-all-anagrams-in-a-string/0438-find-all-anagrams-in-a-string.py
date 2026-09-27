class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s) < len(p):
            return []
        
        t = Counter(p)

        window = Counter(s[:len(p)])
        res = []

        if window == t:
            res.append(0)

        for i in range(len(p), len(s)):
            new = s[i]
            window[new] += 1

            old = s[i- len(p)] 
            window[old] -= 1

            if window[old] == 0:
                del window[old]

            if window == t:
                res.append(i - len(p) + 1)


        return res       

        
