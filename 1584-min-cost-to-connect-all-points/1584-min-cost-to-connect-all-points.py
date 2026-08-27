import heapq as hq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #basically find mst
        #use primms as its a dense graph no needf to sort and find each time like kruskalls

        n = len(points)
        visited = set()
        total_cost = 0
        min_heap = [(0,0)]

        while len(visited) < n:
            cost, u = hq.heappop(min_heap)

            if u in visited: continue

            visited.add(u)
            total_cost += cost

            for v in range(n):
                if v not in visited:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1]) #manhattan diostance
                    hq.heappush(min_heap,(dist,v))

            
        return total_cost