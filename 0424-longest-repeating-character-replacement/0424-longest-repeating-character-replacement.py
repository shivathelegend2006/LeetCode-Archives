class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        left = 0
        longest = 0
        max_f = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right],0) #this creates key and value as 0 if it does not exist

            max_f = max(max_f,count[s[right]])

            while (right - left + 1) - max_f > k:
                count[s[left]] -= 1
                left += 1
                
            longest = max(longest, right - left +1)

        return longest