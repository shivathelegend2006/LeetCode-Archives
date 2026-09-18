class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        x,y,z = target[0],target[1], target[2]
        a,b,c = False, False, False
        for t in triplets:

            if t[0] > x or t[1] > y or t[2] > z:
                continue
            
            if t[0] == x: a = True
            if t[1] == y: b = True
            if t[2] == z: c = True

            if a and b and c:
                return True
        return a and b and c