class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        indices = {}

        for i in range(len(s)):
            if s[i] in indices.keys():
                indices[s[i]].append(i)
            else:
                indices[s[i]] = [i]
        indices = {key: [min(values), max(values)] for key, values in indices.items()}
        #now apply merge intervals
        intervals = list(indices.values())
        intervals.sort(key = lambda x: x[0]) #sort based on starting time

        results = [intervals[0]]
        for curr in intervals[1:]:
            last = results[-1]
            if curr[0] <= last[1]: #if curretn starts before last ends
                last[1] = max(curr[1],last[1])# mergee
            else:
                results.append(curr)
        results = [1+x[1]-x[0] for x in results]
        return results