from collections import defaultdict, Counter
import heapq

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        si = defaultdict(list)
        sc = dict(Counter(s))
        tc = dict(Counter(t))
        if not (Counter(t) <= Counter(s)): return ""
        for i in range(len(s)):
            if tc.get(s[i], 0)  > 0: si[s[i]].append(i)

        min_heap = []
        bd = float('inf')
        cm = float('-inf')
        i,j = 0,-1

        for k, v in si.items():
            for i in range(tc[k]):
                heapq.heappush(min_heap,(v[i],k,i))
                if v[i] > cm: cm = v[i]

        while True:
            c_min, key, indx = heapq.heappop(min_heap)

            cd = cm - c_min
            if cd <= bd:
                bd = cd

                i,j = c_min, cm

            next = indx+ tc[key]
            target = si[key]
            if next >= len(target): break

            heapq.heappush(min_heap,(target[next],key,next))

            if target[next] > cm: cm = target[next]
        

        return s[i:j+1]
            


