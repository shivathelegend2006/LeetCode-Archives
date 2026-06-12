class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removed = 0 # number of meetings to remove
        intervals.sort(key = lambda x: x[1]) #sort based on end times
        #idea is to include meetings that end the earliest withotu ioverlapping
        edge = intervals[0][1]
        x = intervals
        for i in range(1,len(intervals)):
            if x[i][0] < edge: #if the current meeting starts before the previouis one ends
                removed += 1
            else:
                edge = x[i][1] #esle it bcomes the new edge

        return removed