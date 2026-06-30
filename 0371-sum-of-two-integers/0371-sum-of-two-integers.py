class Solution:
    def getSum(self, a: int, b: int) -> int:
        bound = 0xFFFFFFFF #32 bit
        while b != 0:
            carry = (a& b ) << 1

            a, b = (a ^ b) & bound, ((a & b) << 1) & bound

        maxp = 0x7FFFFFFF

        if a > maxp:
            return ~(a^bound)
        else:
            return a