class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums) #we use set as set is like a hash tavble. If we search in list then it uses iteration
        longest = 0
        for n in nums_set:
            if (n-1) not in nums_set: 
                curr = n
                current_streak = 1
                while(curr +1) in nums_set:
                    curr +=1
                    current_streak +=1
                if current_streak > longest:
                    longest  = current_streak
        return longest