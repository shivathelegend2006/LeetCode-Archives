class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p,s in zip(position, speed)]
        fleets = 0
        slowest = 0
        pairs.sort(reverse = True)

        for p,s in pairs:
            t = (target - p)/s
            if t > slowest:
                fleets += 1
                slowest = t

        return fleets
