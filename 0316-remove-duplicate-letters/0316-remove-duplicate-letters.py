from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        hash = Counter(s)
        stack = [s[0]]

        hash[s[0]] -= 1

        present = set()
        present.add(s[0])

        for i in range(1,len(s)):
            hash[s[i]] -= 1
            if s[i] in present: continue

            if s[i] < stack[-1]:
                
                while stack and hash[stack[-1]] > 0 and stack[-1] > s[i]:
                    top = stack[-1]
                    present.remove(top)
                    stack.pop()
                    

            stack.append(s[i])
            present.add(s[i])
            
        
        return "".join(stack)