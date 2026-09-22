from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1: return [0]
        adj = [[] for i in range(n)]
        deg = [0]*n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

            deg[u] += 1
            deg[v] += 1
        l = collections.deque()
        remaining = n
        for i in range(n):
            if deg[i] == 1: l.append(i)
        while remaining > 2:
            lc = len(l)
            remaining -= lc
            for i in range(lc):
                leaf = l.popleft()
                for neighbour in adj[leaf]:
                    deg[neighbour] -= 1
                    if deg[neighbour] == 1:
                        l.append(neighbour)

        return list(l)


