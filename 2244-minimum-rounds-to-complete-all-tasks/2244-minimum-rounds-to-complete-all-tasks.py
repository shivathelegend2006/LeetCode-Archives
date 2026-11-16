from collections import Counter
class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        ht = Counter(tasks)
        count = 0

        for f in ht.values():
            if f == 1: return -1
            r = f % 3
            if r == 0:
                count += f // 3
            else:
                count += f//3
                count += 1

        return count

        