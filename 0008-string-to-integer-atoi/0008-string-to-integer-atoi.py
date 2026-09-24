class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        n = 0
        negative = 0
        leading = 1
        l2 = 1
        for x in s:
            if x == "+" and l2:
                l2 = 0
                continue
            if x == "-" and l2:
                negative = 1
                l2 = 0
                continue
            if not x.isdigit():
                break
            if x == "0" and leading:
                leading = 0
                l2 = 0
                continue
            if x.isdigit():
                l2 = 0
                leading = 0
                n *= 10
                n += int(x)


        if negative:
            n *= -1
            return max(n, -2147483648)

        return min(n, 2147483647)
        