import collections
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = collections.defaultdict(list)

        for u, v, price in flights:
            adj[u].append((v,price)) #adjancry list

        min_cost = [float('inf')]*n
        min_cost[src] = 0

        q = collections.deque([(src,0)]) #queue with the destinaiton and price to get ther
        stops = 0

        while q and stops <= k:
            level = len(q) 
            for _ in range(level):
                city, curr = q.popleft()

                for neighbour, price in adj[city]:
                    new = curr + price
                    if new < min_cost[neighbour]:
                        min_cost[neighbour] = new
                        q.append((neighbour,new))
            stops += 1

        if min_cost[dst] == float('inf'):
            return -1
        return min_cost[dst]