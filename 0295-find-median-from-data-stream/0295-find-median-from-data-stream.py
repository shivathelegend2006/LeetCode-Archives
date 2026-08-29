import bisect # cheatcode to to perform bianry searhc for inserintgub 
class MedianFinder:

    def __init__(self):
        self.arr = []
        self.index = 0

    def addNum(self, num: int) -> None:
        bisect.insort(self.arr, num)

        self.index += 1

    def findMedian(self) -> float:
        isEven = self.index % 2 == 0
        i = self.index
        if isEven:
            a = self.arr[i//2]
            b = self.arr[(i//2) - 1]
            return (a+b)/2
        else:
            return self.arr[i//2]        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()