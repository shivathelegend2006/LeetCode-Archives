class Solution:
    def isHappy(self, n: int) -> bool:
        while True:
            sum = 0
            for i in str(n):
                sum += int(i)**2
            if sum < 10:
                if sum == 1 or sum == 7:
                    return True
                else:
                    return False
            n = sum