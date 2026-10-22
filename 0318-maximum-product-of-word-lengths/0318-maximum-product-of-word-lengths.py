class Solution:
    def maxProduct(self, words: list[str]) -> int:
        ans = 0
        sets = [set(w) for w in words]

        for i in range(0,len(words)- 1):
            for j in range(i+1, len(words)):
                if not(sets[i] & sets[j]):
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans