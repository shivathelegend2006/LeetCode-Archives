import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        heap = []

        for p in primes:
            heapq.heappush(heap, (p* ugly[0], p, 0))

        while len(ugly) < n:
            val, p , i = heapq.heappop(heap)

            if val != ugly[-1]:
                ugly.append(val)

            heapq.heappush(heap,(p*ugly[i+1],p,i+1))

        return ugly[-1]

            
            
        
