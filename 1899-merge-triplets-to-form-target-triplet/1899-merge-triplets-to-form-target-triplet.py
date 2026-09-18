class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        x,y,z = target[0],target[1], target[2]
        a,b,c = False, False, False
        for i in triplets:
            if i[0] == x: a = True
            if i[1] == y: b = True
            if i[2] == z: c = True
        if not( a and b and c): return False

        t = []
        for i in triplets:
            if i[0] > x or i[1] > y or i[2] > z:
                continue
            else:
                t.append(i)

        a,b,c = False, False, False
        for i in t:
            if i[0] == x: a = True
            if i[1] == y: b = True
            if i[2] == z: c = True
        
        if not( a and b and c): return False
        return True