class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cs = set()
        left = 0
        longest = 0
        for right in range(len(s)):
            while s[right] in cs:
                cs.remove(s[left])
                left += 1
            cs.add(s[right])
            if (right - left + 1 > longest):
                longest = right - left +1
        return longest