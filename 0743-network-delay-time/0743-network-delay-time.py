import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))

        heap = [(0,k)] #dist and node
        dist = {}

        while heap:
            d, node = heapq.heappop(heap)

            if node in dist:
                continue

            dist[node] = d

            for nei, weight in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap,(d+weight, nei))
        if len(dist) != n:
            return -1

        return max(dist.values())