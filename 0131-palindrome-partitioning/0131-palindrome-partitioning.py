class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #insane backtrack 
        result = []
        part = []

        def bt(i):
            if i >= len(s):
                result.append(part.copy())
                return

            for j in range(i,len(s)):
                if self.ispal(s,i,j):
                    part.append(s[i:j+1])
                    bt(j+1) # hand the rest
                    part.pop() # backtrack removing the last one to chekc al other combinations

        bt(0)
        return result

    def ispal(self,s,l,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1
        return True