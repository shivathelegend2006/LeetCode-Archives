class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # 1 is a perfect square (1 * 1 = 1)
        if num < 2:
            return True
            
        left, right = 2, num // 2
        
        while left <= right:
            mid = left + (right - left) // 2
            squared = mid * mid
            
            if squared == num:
                return True
            elif squared > num:
                right = mid - 1
            else:
                left = mid + 1
                
        return False