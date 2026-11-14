from collections import Counter
class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n = len(s) // k
        sc = Counter(s[i: i+n] for i in range(0, len(s), n))
        tc = Counter(t[i: i+n] for i in range(0, len(s), n))
        return sc == tc