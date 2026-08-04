from collections import Counter
class DetectSquares:

    def __init__(self):
        self.pts = Counter()

    def add(self, point: List[int]) -> None:
        self.pts[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        px, py = point
        totalSq = 0

        for (x,y), count in self.pts.items():
            if x!= px and abs(px-x) == abs(py-y):
                corner1 = self.pts[(x,py)]
                corner2 = self.pts[(px,y)]

                totalSq += count* corner1* corner2

        return totalSq


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)