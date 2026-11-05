class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        reservedSeats.sort()

        s = set()


        count = (reservedSeats[0][0] - 1)*2
        s1 = {2,3,4,5}
        s2 = {4,5,6,7}
        s3 = {6,7,8,9}
        pre = reservedSeats[0][0]
        pre_s = 0
        for r,c in reservedSeats:
            if r == pre:
                s.add(c)
                continue
            else:
                pre_s = c
                f1 = False
                f2 = False
                f3 = False

                if not(s1 & s): f1 = True
                if not(s2 & s): f2 = True
                if not(s3 & s): f3 = True

                if(f1 and f3): count += 2
                elif (f2 or f1 or f3): count += 1
                else: count += 0

                s.clear()
                count += (r - pre - 1)*2
                pre = r
                s.add(pre_s)

        if s:
            f1 = False
            f2 = False
            f3 = False

            if not(s1 & s): f1 = True
            if not(s2 & s): f2 = True
            if not(s3 & s): f3 = True

            if(f1 and f3): count += 2
            elif (f2 or f1 or f3): count += 1
            else: count += 0
        count += (n - pre) * 2
        return count 