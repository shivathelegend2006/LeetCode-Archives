from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #just use maths bro
        freq = Counter(tasks)
        maxFreq = max(freq.values())
        nums_max_freq = sum(1 for c in freq.values() if c == maxFreq)

        total = (maxFreq - 1)*(n+1) + nums_max_freq

        return max(len(tasks),total)