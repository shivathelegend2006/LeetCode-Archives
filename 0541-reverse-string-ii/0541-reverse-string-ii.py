class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Convert string to a list because Python strings are immutable
        chars = list(s)
        
        # Step through the list in increments of 2k
        for i in range(0, len(chars), 2 * k):
            # Reverse the first k characters of the current 2k chunk
            chars[i:i + k] = reversed(chars[i:i + k])
            
        return "".join(chars)