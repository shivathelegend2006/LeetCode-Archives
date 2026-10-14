class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3: return False
        
        def verify(n1,n2,tape):
            if tape == "": return True

            n3 = str(n1 + n2)

            if tape.startswith(n3):
                remaining  = tape[len(n3):]
                return verify(n2, int(n3), remaining)
            return False

        
        for i in range(1, len(num)):
            for j in range(i+1, len(num)):

                n1 = num[:i]
                n2 = num[i:j]

                if (len(n1) > 1 and n1[0] == "0") or (len(n2)>1 and n2[0] == "0"):
                    continue

                if verify(int(n1), int(n2), num[j:]): return True

        return False