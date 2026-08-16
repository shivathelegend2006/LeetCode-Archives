class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort()
        self.top_k = nums[-k:] if nums else []   

    def add(self, val: int) -> int:
        left, right = 0, len(self.top_k)
        
        while left < right:
            mid = (left + right) // 2
            if self.top_k[mid] < val:
                left = mid + 1
            else:
                right = mid
                

        self.top_k.insert(left, val)
        

        if len(self.top_k) > self.k:
            self.top_k.pop(0)
        return self.top_k[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)