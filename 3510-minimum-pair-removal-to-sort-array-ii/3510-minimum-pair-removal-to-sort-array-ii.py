import heapq
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=1: return 0

        left_neighbour = {i:i-1 for i in range(n)}
        right_neighbour = {i:i+1 for i in range(n)}
        
        left_neighbour[0] = -1
        right_neighbour[n-1] = -1

        val = nums[:]
        version = [0] * n
        heap = []
        unsorted = 0

        for i in range(n-1):
            if val[i] > val[i+1]:
                unsorted += 1
            heapq.heappush(heap, (val[i] + val[i+1], i, i+1, 0, 0))

        count = 0

        while unsorted > 0 and  heap:
            s, i, j, vi, vj = heapq.heappop(heap)

            if version[i] != vi or version[j] != vj:
                continue

            left  = left_neighbour[i]
            right = right_neighbour[j]

            if left != -1 and val[left] > val[i]: unsorted -=1
            if val[i] > val[j] : unsorted -= 1
            if right != -1 and val[j] > val[right]: unsorted -= 1

            val[i] += val[j]
            version[i] += 1
            version[j] += 1

            right_neighbour[i] = right

            if right != -1:
                left_neighbour[right] = i

            if left != -1 and val[left] > val[i]: unsorted += 1
            if right != -1 and val[i] > val[right]: unsorted += 1

            if left != -1:
                heapq.heappush(heap, (val[left] + val[i], left, i, version[left], version[i]))
            if right != -1:
                heapq.heappush(heap, (val[i] + val[right], i, right, version[i], version[right]))

            count += 1

        return count