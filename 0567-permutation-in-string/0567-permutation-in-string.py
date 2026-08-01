from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)> len(s2): return False

        target = Counter(s1) #return a dictionary with exac occurance of eahc letter
        n = len(s1)
        window = Counter(s2[:n])

        if window == target: return True

        for i in range(n,len(s2)):
            char = s2[i]
            window[char] += 1

            old_char = s2[i-n]
            window[old_char] -= 1

            if window[old_char] == 0:
                del window[old_char]

            if window == target: return True

        return False
