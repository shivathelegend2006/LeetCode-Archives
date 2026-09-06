import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for i in nums:
            heapq.heappush(min_heap,i)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return heapq.heappop(min_heap)

        '''
        the most direct approach is using min heap
        min heap automaticallys tores such that the binary tree all parents will be lesser than children

        so first store till k elements are filled
        next for the ith element kick out the smallst and replace with the ith if i is > k which ensure at every step the k most largets only stays in the min heap

        finally return the top of the tree as the kth larghest
        u can do it without heap but hep is the most direct approach
        '''