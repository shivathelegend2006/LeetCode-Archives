class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0

        def count_palindromes(l,r):
            c = 0
            while l >=0 and r < len(s) and s[l] == s[r]:
                c+=1
                l -= 1
                r += 1

            return c

        for i in range(len(s)):
            count += count_palindromes(i,i)
            count += count_palindromes(i,i+1)

        return count
        