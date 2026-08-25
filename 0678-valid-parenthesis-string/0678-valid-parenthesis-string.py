class Solution:
    def checkValidString(self, s: str) -> bool:
        #use maaaaaath'
        l_min = 0
        l_max = 0

        for i in s:
            if i == "(":
                l_min += 1
                l_max += 1
            elif i == ")":
                l_min -= 1
                l_max -= 1
            else:
                l_min -= 1
                l_max += 1
            
            if l_max < 0:
                return False  
            if l_min < 0: 
                l_min = 0 

        return l_min == 0